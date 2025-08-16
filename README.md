# vibeutils

A Python library that counts letter frequency and compares numbers using OpenAI API.

## Features

- Count frequency of specific letters in text
- Compare two numbers using AI
- Case-sensitive and case-insensitive counting options
- Uses OpenAI API for intelligent processing
- Easy to use API
- Ready for PyPI distribution

## Installation

Install the package using pip:

```bash
pip install vibeutils
```

## Setup

You need to provide your own OpenAI API key. Set it as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Letter Counting - vibecount()

```python
from vibeutils import vibecount

# Count letter 'r' in "strawberry" (case-sensitive by default)
result = vibecount("strawberry", "r")
print(result)  # 2 ;)

# Case-insensitive counting
result = vibecount("Strawberry", "R", case_sensitive=False)
print(result)  # 2 ;)

# Case-sensitive counting (explicit)
result = vibecount("Strawberry", "R", case_sensitive=True)
print(result)  # 0 (no uppercase 'R' in "Strawberry")
```

### Number Comparison - vibecompare()

```python
from vibeutils import vibecompare

# Compare two integers
result = vibecompare(5, 10)
print(result)  # -1 (first number is smaller)

# Compare two floats
result = vibecompare(3.14, 2.71)
print(result)  # 1 (first number is larger)

# Compare equal numbers
result = vibecompare(7, 7)
print(result)  # 0 (numbers are equal)
```

### Parameters

#### vibecount(text, target_letter, case_sensitive=True)
- `text` (str): The input string to analyze
- `target_letter` (str): The letter to count (must be a single character)
- `case_sensitive` (bool, optional): Whether to perform case-sensitive counting (default: True)

#### vibecompare(num1, num2)
- `num1` (Union[int, float]): The first number to compare
- `num2` (Union[int, float]): The second number to compare

### Return Values

- **vibecount()**: Returns an integer representing the count of the target letter
- **vibecompare()**: Returns an integer:
  - `-1` if the first number is smaller than the second
  - `0` if the numbers are equal
  - `1` if the first number is larger than the second

### Error Handling

Both functions raise:
- `ValueError`: If OpenAI API key is not set or invalid arguments provided
- `Exception`: If OpenAI API call fails

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls

## Dependencies

- `openai>=1.0.0`

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
pytest tests/test_vibecount.py
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

This package uses the OpenAI API for processing, which requires an API key and internet connection. Each function call will make a request to OpenAI's servers and will consume API credits.
