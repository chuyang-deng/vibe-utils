"""
Example usage of vibeutils package
"""

import os
from vibeutils import vibecount, vibecompare

def main():
    # Make sure to set your OpenAI API key first
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable")
        print("export OPENAI_API_KEY=your_key_here")
        return
    
    print("=== vibecount examples ===")
    
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
    
    print("\n=== vibecompare examples ===")
    
    # Example 4: Compare integers
    num1, num2 = 5, 10
    result = vibecompare(num1, num2)
    comparison_text = {-1: "smaller than", 0: "equal to", 1: "larger than"}[result]
    print(f"{num1} is {comparison_text} {num2} (result: {result})")
    
    # Example 5: Compare floats
    num1, num2 = 3.14, 2.71
    result = vibecompare(num1, num2)
    comparison_text = {-1: "smaller than", 0: "equal to", 1: "larger than"}[result]
    print(f"{num1} is {comparison_text} {num2} (result: {result})")
    
    # Example 6: Compare equal numbers
    num1, num2 = 7, 7
    result = vibecompare(num1, num2)
    comparison_text = {-1: "smaller than", 0: "equal to", 1: "larger than"}[result]
    print(f"{num1} is {comparison_text} {num2} (result: {result})")

if __name__ == "__main__":
    main()
