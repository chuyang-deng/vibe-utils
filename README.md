# vibeutils

A Python utils library that counts letter frequency, gets string length, compares numbers, and evaluates mathematical expressions using OpenAI and Anthropic APIs.

## Features

- Count frequency of specific letters in text
- Get the length of a string
- Compare two numbers using AI
- Evaluate mathematical expressions safely
- Support for both OpenAI and Anthropic APIs
- Environment variable support for default provider selection
- Custom model selection via parameters or environment variables

## Quick Start

```python
from vibeutils import vibecount, vibecompare, vibeeval, vibelength

# Set your preferred provider globally (optional)
# export VIBEUTILS_PROVIDER=anthropic

# Now all function calls use your preferred provider automatically
count = vibecount("strawberry", "r")        # Count letter frequency
length = vibelength("strawberry")            # Get string length
comparison = vibecompare(5, 10)               # Compare numbers  
result = vibeeval("(2 + 3) * 4")             # Evaluate expressions
```

## Upcoming

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

#### Custom Models (Optional)
You can specify custom models for each provider:

```bash
export VIBEUTILS_OPENAI_MODEL=gpt-4                    # Use GPT-4 instead of default
export VIBEUTILS_ANTHROPIC_MODEL=claude-opus-4-20250514  # Use Claude Opus instead of default
```

### Provider and Model Selection

By default, all functions use OpenAI with the default model. You can specify both provider and model in multiple ways:

#### Method 1: Environment Variables (Recommended)
Set environment variables to avoid specifying the provider and model in every function call:

```bash
# Provider selection
export VIBEUTILS_PROVIDER=anthropic  # Use Anthropic as default provider
export VIBEUTILS_PROVIDER=openai     # Use OpenAI as default provider (or just unset)

# Model selection
export VIBEUTILS_OPENAI_MODEL=gpt-4                    # Custom OpenAI model
export VIBEUTILS_ANTHROPIC_MODEL=claude-3-opus-20240229  # Custom Anthropic model
```

#### Method 2: Function Parameters
You can override environment variables using function parameters:

```python
# Provider and model parameters
vibecount("test", "t", provider="openai", model="gpt-4")
vibecompare(5, 10, provider="anthropic", model="claude-3-haiku-20240307")
vibeeval("2+3", provider="openai", model="gpt-4-turbo")
```

#### Priority Order for Provider Selection
1. **Explicit provider parameter** (highest priority)
2. **VIBEUTILS_PROVIDER environment variable**
3. **Default to "openai"** (lowest priority)

#### Priority Order for Model Selection
1. **Explicit model parameter** (highest priority)
2. **Environment variable** (VIBEUTILS_OPENAI_MODEL or VIBEUTILS_ANTHROPIC_MODEL)
3. **Built-in defaults** (gpt-4o-mini for OpenAI, claude-sonnet-4-20250514 for Anthropic)

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

# Using custom models
result = vibecount("strawberry", "r", provider="openai", model="gpt-4")
print(result)  # 2 (using GPT-4 model)

result = vibecount("strawberry", "r", provider="anthropic", model="claude-3-opus-20240229")
print(result)  # 2 (using Claude Opus model)
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

# Using custom models
result = vibecompare(15, 10, provider="openai", model="gpt-4-turbo")
print(result)  # 1 (using GPT-4 Turbo model)

result = vibecompare(3.14, 2.71, provider="anthropic", model="claude-3-haiku-20240307")
print(result)  # 1 (using Claude Haiku model)
```

### String Length - vibelength()

```python
from vibeutils import vibelength

# Get length (uses default provider)
result = vibelength("strawberry")
print(result)  # 10

# Using environment variable to set default provider
# export VIBEUTILS_PROVIDER=anthropic
result = vibelength("strawberry")  # Now uses Anthropic automatically
print(result)  # 10

# Override environment variable with explicit provider
result = vibelength("strawberry", provider="openai")  # Forces OpenAI
print(result)  # 10

# Using custom models
result = vibelength("hello world", provider="openai", model="gpt-4")
print(result)  # 11

result = vibelength("HELLO", provider="anthropic", model="claude-3-haiku-20240307")
print(result)  # 5
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

# Using custom models
result = vibeeval("2 ** 8", provider="openai", model="gpt-4")
print(result)  # 256.0 (using GPT-4 model)

result = vibeeval("sqrt(16)", provider="anthropic", model="claude-3-sonnet-20240229")
# Note: sqrt function may not be supported - depends on model understanding
```

### Parameters

#### vibecount(text, target_letter, case_sensitive=True, provider=None, model=None)
- `text` (str): The input string to analyze
- `target_letter` (str): The letter to count (must be a single character)
- `case_sensitive` (bool, optional): Whether to perform case-sensitive counting (default: True)
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.
- `model` (str, optional): The model to use for the provider. If None, uses environment variables VIBEUTILS_OPENAI_MODEL or VIBEUTILS_ANTHROPIC_MODEL, defaulting to built-in constants if not set.

#### vibecompare(num1, num2, provider=None, model=None)
- `num1` (Union[int, float]): The first number to compare
- `num2` (Union[int, float]): The second number to compare
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.
- `model` (str, optional): The model to use for the provider. If None, uses environment variables VIBEUTILS_OPENAI_MODEL or VIBEUTILS_ANTHROPIC_MODEL, defaulting to built-in constants if not set.

#### vibelength(text, provider=None, model=None)
- `text` (str): The input string to measure the length of
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.
- `model` (str, optional): The model to use for the provider. If None, uses environment variables VIBEUTILS_OPENAI_MODEL or VIBEUTILS_ANTHROPIC_MODEL, defaulting to built-in constants if not set.

#### vibeeval(expression, provider=None, model=None)
- `expression` (str): Mathematical expression containing numbers, operators (+, -, *, /, **), and parentheses
- `provider` (str, optional): AI provider to use ("openai" or "anthropic"). If None, uses VIBEUTILS_PROVIDER environment variable, defaulting to "openai" if not set.
- `model` (str, optional): The model to use for the provider. If None, uses environment variables VIBEUTILS_OPENAI_MODEL or VIBEUTILS_ANTHROPIC_MODEL, defaulting to built-in constants if not set.

### Return Values

- **vibecount()**: Returns an integer representing the count of the target letter
- **vibelength()**: Returns an integer representing the number of characters in the input string
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

### Provider and Model-Specific Notes

#### Default Models
- **OpenAI**: Uses `gpt-4o-mini` model by default
- **Anthropic**: Uses `claude-sonnet-4-20250514` model by default

#### Custom Model Support
- **OpenAI**: Supports available OpenAI models (e.g., `gpt-4`, `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`, `o1-preview`, `o1-mini`)
- **Anthropic**: Supports any valid Anthropic model (e.g., `claude-3-opus-20240229`, `claude-3-sonnet-20240229`, `claude-3-haiku-20240307`)

#### Model Selection Methods
1. **Function parameter**: `model="gpt-4"` (highest priority)
2. **Environment variable**: `VIBEUTILS_OPENAI_MODEL=gpt-4` (medium priority)
3. **Built-in default**: Uses package defaults (lowest priority)

#### Model Compatibility and API Parameters
- **Automatic Parameter Handling**: The library automatically detects model capabilities and uses the appropriate API parameters
- **Legacy Models** (gpt-3.5-turbo, gpt-4, gpt-4-turbo): Use `max_tokens` parameter, support `temperature=0`
- **Newer Models** (gpt-4o, gpt-4o-mini): Use `max_completion_tokens` parameter, support `temperature=0`
- **o1 Models**: Special handling - use `max_completion_tokens`, no `temperature` parameter supported
- **Future-Proof**: Automatically handles new OpenAI models with updated API requirements

#### Security and Validation
- All providers implement the same security checks and response validation
- Model selection does not affect security features
- Custom models must still support the expected input/output format
- API parameter compatibility is handled automatically based on model type
