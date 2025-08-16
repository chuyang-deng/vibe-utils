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
            model="gpt-4o-mini",
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


def vibecompare(num1: Union[int, float], num2: Union[int, float]) -> int:
    """
    Compare two numbers using OpenAI API.
    
    Args:
        num1 (Union[int, float]): The first number to compare
        num2 (Union[int, float]): The second number to compare
    
    Returns:
        int: -1 if num1 < num2, 0 if num1 == num2, 1 if num1 > num2
    
    Raises:
        ValueError: If OpenAI API key is not set or inputs are not numbers
        Exception: If OpenAI API call fails
    """
    # Validate inputs
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers (int or float)")
    
    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    # Set up OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    prompt = f"""Compare the two numbers {num1} and {num2}.
Return:
- -1 if the first number ({num1}) is smaller than the second number ({num2})
- 0 if the numbers are equal
- 1 if the first number ({num1}) is larger than the second number ({num2})

Only return the number (-1, 0, or 1) as your response, nothing else.
"""
    
    try:
        # Make API call to OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0
        )
        
        # Extract and return the comparison result
        result = response.choices[0].message.content.strip()
        comparison_result = int(result)
        
        # Validate the result is one of the expected values
        if comparison_result not in [-1, 0, 1]:
            raise Exception(f"OpenAI API returned invalid comparison result: {result}")
        
        return comparison_result
        
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            raise Exception(f"OpenAI API returned unexpected response: {result}")
        raise e
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {str(e)}")
