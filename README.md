# vibeutils

A Python utils library that counts letter frequency, compares numbers, and evaluates mathematical expressions using OpenAI and Anthropic APIs.

## Features

- Count frequency of specific letters in text
- Compare two numbers using AI
- Evaluate mathematical expressions safely
- Support for both OpenAI and Anthropic APIs
- Environment variable support for default provider selection

## Quick Start

```python
from vibeutils import vibecount, vibecompare, vibeeval

# Set your preferred provider globally (optional)
# export VIBEUTILS_PROVIDER=anthropic

# Now all function calls use your preferred provider automatically
count = vibecount("strawberry", "r")        # Count letter frequency
comparison = vibecompare(5, 10)             # Compare numbers  
result = vibeeval("(2 + 3) * 4")            # Evaluate expressions
```

## Upcoming

* `vibelength()`
* `viebtime`
* ...

## Performance

- Time complexity: O(luck) and I use API calls to prevent prompt injection.

## Installation

Install the package using pip:

```bash
pip install vibeutils
```

For Anthropic support, install with the optional dependency:

```bash
pip install "vibeutils[anthropic]"
```

## Setup

Set up vibeutils in 3 easy steps:

1. **Install the package** (see Installation section)
2. **Set API keys** for your chosen provider(s)
3. **Optionally set default provider** to avoid specifying it in every call

### API Keys

You need to provide API keys for the services you want to use.

#### OpenAI (Default Provider)
Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

#### Anthropic (Optional)
To use Anthropic's Claude, set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

#### Default Provider (Optional)
To avoid specifying the provider in every function call, you can set a default provider:

```bash
export VIBEUTILS_PROVIDER=anthropic  # Use Anthropic as default
# or
export VIBEUTILS_PROVIDER=openai     # Use OpenAI as default (same as not setting it)
```

### Provider Selection

By default, all functions use OpenAI. You can specify a provider in multiple ways:

#### Method 1: Environment Variable (Recommended)
Set the `VIBEUTILS_PROVIDER` environment variable to avoid specifying the provider in every function call:

```bash
# Use Anthropic as the default provider
export VIBEUTILS_PROVIDER=anthropic

# Use OpenAI as the default provider (or just unset the variable)
export VIBEUTILS_PROVIDER=openai
# or
unset VIBEUTILS_PROVIDER
```

#### Method 2: Provider Parameter
You can still override the environment variable by using the `provider` parameter:

- `provider="openai"`
- `provider="anthropic"`

#### Priority Order
1. **Explicit provider parameter** (highest priority)
2. **VIBEUTILS_PROVIDER environment variable**
3. **Default to "openai"** (lowest priority)

## Usage

### Letter Counting - vibecount()

```python
from vibeutils import vibecount

# Count letter 'r' in "strawberry" (uses default provider)
result = vibecount("strawberry", "r")
print(result)  # 2 ;)

# Using environment variable to set default provider
# export VIBEUTILS_PROVIDER=anthropic
result = vibecount("strawberry", "r")  # Now uses Anthropic automatically
print(result)  # 2 ;)

# Override environment variable with explicit provider
result = vibecount("strawberry", "r", provider="openai")  # Forces OpenAI
print(result)  # 2 ;)

# Case-insensitive counting
result = vibecount("Strawberry", "R", case_sensitive=False)
print(result)  # 2 ;)

# Case-insensitive counting with explicit provider
result = vibecount("Strawberry", "R", case_sensitive=False, provider="anthropic")
print(result)  # 2 ;)

# Case-sensitive counting (explicit)
result = vibecount("Strawberry", "R", case_sensitive=True, provider="openai")
print(result)  # 0 (no uppercase 'R' in "Strawberry")
```

### Number Comparison - vibecompare()

```python
from vibeutils import vibecompare

# Compare two integers (uses default provider)
result = vibecompare(5, 10)
print(result)  # -1 (first number is smaller)

# Using environment variable to set default provider
# export VIBEUTILS_PROVIDER=anthropic
result = vibecompare(5, 10)  # Now uses Anthropic automatically
print(result)  # -1 (first number is smaller)

# Compare two floats
result = vibecompare(5.11, 5.9)
print(result)  # -1 ;)

# Override environment variable with explicit provider
result = vibecompare(7, 7, provider="openai")  # Forces OpenAI
print(result)  # 0 (numbers are equal)
```

### Mathematical Expression Evaluation - vibeeval()

```python
from vibeutils import vibeeval

# Basic arithmetic operations (uses default provider)
result = vibeeval("2 + 3")
print(result)  # 5.0

# Using environment variable to set default provider
# export VIBEUTILS_PROVIDER=anthropic
result = vibeeval("3 * 4")  # Now uses Anthropic automatically
print(result)  # 12.0

# Complex expressions with parentheses
result = vibeeval("(2 + 3) * 4")
print(result)  # 20.0

# Override environment variable with explicit provider
result = vibeeval("5 / 2", provider="openai")  # Forces OpenAI
print(result)  # 2.5

# Error handling for invalid expressions
try:
    result = vibeeval("2 +")  # Invalid syntax
except ValueError as e:
    print(f"Error: {e}")

try:
    result = vibeeval("1 / 0")  # Division by zero
except ValueError as e:
    print(f"Error: {e}")
```

### Parameters

#### vibecount(text, target_letter, case_sensitive=True, provider=None)
- `text` (str): The input string to analyze
- `target_letter` (str): The letter to count (must be a single character)
- `case_sensitive` (bool, optional): Whether to perform case-sensitive counting (default: True)
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.

#### vibecompare(num1, num2, provider=None)
- `num1` (Union[int, float]): The first number to compare
- `num2` (Union[int, float]): The second number to compare
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.

#### vibeeval(expression, provider=None)
- `expression` (str): Mathematical expression containing numbers, operators (+, -, *, /, **), and parentheses
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.

### Return Values

- **vibecount()**: Returns an integer representing the count of the target letter
- **vibecompare()**: Returns an integer:
  - `-1` if the first number is smaller than the second
  - `0` if the numbers are equal
  - `1` if the first number is larger than the second
- **vibeeval()**: Returns a float representing the result of the mathematical expression

### Error Handling

All functions raise:
- `ValueError`: If API key is not set for the chosen provider, invalid arguments provided, or invalid mathematical expression (vibeeval only)
- `ImportError`: If the anthropic package is not installed when using provider="anthropic"
- `Exception`: If AI API call fails or response validation fails

## Requirements

- Python 3.8+
- OpenAI API key (for OpenAI provider)
- Anthropic API key (for Anthropic provider, optional)
- Internet connection for API calls

## Dependencies

### Required
- `openai>=1.0.0`

### Optional (for Anthropic support)
- `anthropic>=0.3.0`

## Development

### Running Tests

Install test dependencies:
```bash
pip install -r test-requirements.txt
```

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=vibeutils
```

Run specific test file:
```bash
pytest tests/test_vibeutils.py
```

### Test Structure

The test suite includes:
- Unit tests for all function parameters and edge cases
- Mock tests for OpenAI API calls (no actual API calls during testing)
- Error handling validation
- Input validation tests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Note

This package uses AI APIs for processing, which require API keys and internet connection. Each function call will make multiple requests to the chosen AI provider's servers and will consume API credits.

### Provider-Specific Notes

- **OpenAI**: Uses GPT-4o-mini model for all operations
- **Anthropic**: Uses Claude-3.5-Sonnet model for all operations
- All providers implement the same security checks and response validation
