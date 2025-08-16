"""
Core functionality for vibeutils package
"""

import os
import openai
from typing import Union


def vibecount(text: str, target_letter: str, case_sensitive: bool = True) -> int:
    """
    Count the frequency of a specific letter in a string using OpenAI API.
    
    Args:
        text (str): The input string to analyze
        target_letter (str): The letter to count (should be a single character)
        case_sensitive (bool): Whether to perform case-sensitive counting (default: True)
    
    Returns:
        int: The count of the target letter in the text
    
    Raises:
        ValueError: If OpenAI API key is not set or target_letter is not a single character
        Exception: If OpenAI API call fails
    """
    # Validate inputs
    if not isinstance(target_letter, str) or len(target_letter) != 1:
        raise ValueError("target_letter must be a single character")
    
    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    # Set up OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    # Prepare the prompt based on case sensitivity
    case_instruction = "case-sensitive" if case_sensitive else "case-insensitive"
    
    prompt = f"""Count how many times the letter '{target_letter}' appears in the following text. 
The counting should be {case_instruction}.
Only return the number as your response, nothing else.

Text: "{text}"
"""
    
    try:
        # Make API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0
        )
        
        # Extract and return the count
        result = response.choices[0].message.content.strip()
        return int(result)
        
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            raise Exception(f"OpenAI API returned unexpected response: {result}")
        raise e
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {str(e)}")
