"""
Example usage of vibeutils package
"""

import os
from vibeutils import vibecount

def main():
    # Make sure to set your OpenAI API key first
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable")
        print("export OPENAI_API_KEY=your_key_here")
        return
    
    # Example 1: Case-sensitive counting (default)
    text = "strawberry"
    letter = "r"
    count = vibecount(text, letter)
    print(f"Letter '{letter}' appears {count} times in '{text}' (case-sensitive)")
    
    # Example 2: Case-insensitive counting
    text = "Strawberry"
    letter = "R"
    count = vibecount(text, letter, case_sensitive=False)
    print(f"Letter '{letter}' appears {count} times in '{text}' (case-insensitive)")
    
    # Example 3: Case-sensitive counting with mixed case
    text = "Strawberry"
    letter = "R"
    count = vibecount(text, letter, case_sensitive=True)
    print(f"Letter '{letter}' appears {count} times in '{text}' (case-sensitive)")

if __name__ == "__main__":
    main()
