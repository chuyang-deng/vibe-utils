"""
Example usage of vibeutils package with multiple AI providers
"""

import os
from vibeutils import vibecount, vibecompare, vibeeval

def check_api_keys():
    """Check which API keys are available"""
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    has_anthropic = bool(os.getenv("ANTHROPIC_API_KEY"))
    current_provider = os.getenv("VIBEUTILS_PROVIDER", "openai")
    
    print("=== API Key Status ===")
    print(f"OpenAI API Key: {'✓' if has_openai else '✗'}")
    print(f"Anthropic API Key: {'✓' if has_anthropic else '✗'}")
    print(f"VIBEUTILS_PROVIDER: {current_provider}")
    
    if not has_openai and not has_anthropic:
        print("\nPlease set at least one API key:")
        print("export OPENAI_API_KEY=your_openai_key_here")
        print("export ANTHROPIC_API_KEY=your_anthropic_key_here")
        print("\nOptionally set the default provider:")
        print("export VIBEUTILS_PROVIDER=anthropic  # or 'openai' (default)")
        return False
    
    return has_openai, has_anthropic

def run_vibecount_examples(has_openai, has_anthropic):
    """Run vibecount examples with available providers"""
    print("\n=== vibecount examples ===")
    
    text = "strawberry"
    letter = "r"
    
    if has_openai:
        print(f"\n--- OpenAI Provider ---")
        count = vibecount(text, letter, provider="openai")
        print(f"Letter '{letter}' appears {count} times in '{text}' (case-sensitive, OpenAI)")
        
        # Case-insensitive example
        text2 = "Strawberry"
        letter2 = "R"
        count2 = vibecount(text2, letter2, case_sensitive=False, provider="openai")
        print(f"Letter '{letter2}' appears {count2} times in '{text2}' (case-insensitive, OpenAI)")
    
    if has_anthropic:
        print(f"\n--- Anthropic Provider ---")
        count = vibecount(text, letter, provider="anthropic")
        print(f"Letter '{letter}' appears {count} times in '{text}' (case-sensitive, Anthropic)")
        
        # Case-insensitive example
        text2 = "Strawberry"
        letter2 = "R"
        count2 = vibecount(text2, letter2, case_sensitive=False, provider="anthropic")
        print(f"Letter '{letter2}' appears {count2} times in '{text2}' (case-insensitive, Anthropic)")

def run_vibecompare_examples(has_openai, has_anthropic):
    """Run vibecompare examples with available providers"""
    print("\n=== vibecompare examples ===")
    
    comparison_text = {-1: "smaller than", 0: "equal to", 1: "larger than"}
    
    if has_openai:
        print(f"\n--- OpenAI Provider ---")
        # Compare integers
        num1, num2 = 5, 10
        result = vibecompare(num1, num2, provider="openai")
        print(f"{num1} is {comparison_text[result]} {num2} (result: {result}, OpenAI)")
        
        # Compare floats
        num1, num2 = 3.14, 2.71
        result = vibecompare(num1, num2, provider="openai")
        print(f"{num1} is {comparison_text[result]} {num2} (result: {result}, OpenAI)")
    
    if has_anthropic:
        print(f"\n--- Anthropic Provider ---")
        # Compare integers
        num1, num2 = 5, 10
        result = vibecompare(num1, num2, provider="anthropic")
        print(f"{num1} is {comparison_text[result]} {num2} (result: {result}, Anthropic)")
        
        # Compare equal numbers
        num1, num2 = 7, 7
        result = vibecompare(num1, num2, provider="anthropic")
        print(f"{num1} is {comparison_text[result]} {num2} (result: {result}, Anthropic)")

def run_vibeeval_examples(has_openai, has_anthropic):
    """Run vibeeval examples with available providers"""
    print("\n=== vibeeval examples ===")
    
    if has_openai:
        print(f"\n--- OpenAI Provider ---")
        # Basic arithmetic
        result = vibeeval("2 + 3", provider="openai")
        print(f"2 + 3 = {result} (OpenAI)")
        
        # Complex expression
        result = vibeeval("(5 * 2) + 3", provider="openai")
        print(f"(5 * 2) + 3 = {result} (OpenAI)")
        
        # Division with decimal result
        result = vibeeval("7 / 2", provider="openai")
        print(f"7 / 2 = {result} (OpenAI)")
    
    if has_anthropic:
        print(f"\n--- Anthropic Provider ---")
        # Basic arithmetic
        result = vibeeval("3 * 4", provider="anthropic")
        print(f"3 * 4 = {result} (Anthropic)")
        
        # Complex expression with parentheses
        result = vibeeval("(2 + 3) * 4", provider="anthropic")
        print(f"(2 + 3) * 4 = {result} (Anthropic)")
        
        # Error handling example
        try:
            result = vibeeval("1 / 0", provider="anthropic")
            print(f"1 / 0 = {result} (Anthropic)")
        except ValueError as e:
            print(f"Error with 1 / 0: {e} (Anthropic)")

def run_environment_variable_examples():
    """Demonstrate environment variable usage"""
    current_provider = os.getenv("VIBEUTILS_PROVIDER", "openai")
    print(f"\n=== Environment Variable Examples ===")
    print(f"Current VIBEUTILS_PROVIDER: {current_provider}")
    
    # Check if the current provider's API key is available
    if current_provider == "openai" and not os.getenv("OPENAI_API_KEY"):
        print("Skipped - OpenAI API key not available")
        return
    elif current_provider == "anthropic" and not os.getenv("ANTHROPIC_API_KEY"):
        print("Skipped - Anthropic API key not available")
        return
    
    print(f"(Using {current_provider} provider from environment variable - no provider parameter specified)")
    
    # These will use the provider specified in VIBEUTILS_PROVIDER environment variable
    count = vibecount("hello", "l")
    print(f"vibecount('hello', 'l') = {count}")
    
    result = vibecompare(8, 3)
    print(f"vibecompare(8, 3) = {result}")
    
    result = vibeeval("10 - 4")
    print(f"vibeeval('10 - 4') = {result}")

def run_backward_compatibility_examples():
    """Demonstrate backward compatibility (OpenAI default)"""
    if not os.getenv("OPENAI_API_KEY"):
        print("\n=== Backward Compatibility Examples ===")
        print("Skipped - OpenAI API key not available")
        return
    
    print("\n=== Backward Compatibility Examples ===")
    print("(Using explicit OpenAI provider parameter)")
    
    # These work exactly like before, explicitly specifying OpenAI
    count = vibecount("hello", "l", provider="openai")
    print(f"vibecount('hello', 'l', provider='openai') = {count}")
    
    result = vibecompare(8, 3, provider="openai")
    print(f"vibecompare(8, 3, provider='openai') = {result}")
    
    result = vibeeval("10 - 4", provider="openai")
    print(f"vibeeval('10 - 4', provider='openai') = {result}")

def main():
    """Main example function"""
    api_status = check_api_keys()
    if not api_status:
        return
    
    has_openai, has_anthropic = api_status
    
    try:
        run_vibecount_examples(has_openai, has_anthropic)
        run_vibecompare_examples(has_openai, has_anthropic)
        run_vibeeval_examples(has_openai, has_anthropic)
        run_environment_variable_examples()
        run_backward_compatibility_examples()
        
        print("\n=== Summary ===")
        print("✓ All examples completed successfully!")
        print("✓ Both providers work with the same interface")
        print("✓ Environment variable support added (VIBEUTILS_PROVIDER)")
        print("✓ Backward compatibility maintained")
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("This might be due to:")
        print("- Network connectivity issues")
        print("- Invalid API keys")
        print("- API rate limits")
        print("- Missing anthropic package (install with: pip install anthropic)")

if __name__ == "__main__":
    main()
