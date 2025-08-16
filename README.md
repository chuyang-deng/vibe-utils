# vibecount

A Python library that counts the frequency of letters in a string using OpenAI API.

## Features

- Count frequency of specific letters in text
- Case-sensitive and case-insensitive counting options
- Uses OpenAI API for intelligent letter counting
- Easy to use API
- Ready for PyPI distribution

## Installation

Install the package using pip:

```bash
pip install vibecount
```

## Setup

You need to provide your own OpenAI API key. Set it as an environment variable:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Basic Usage

```python
from vibecount import vibecount

# Count letter 'r' in "strawberry" (case-sensitive by default)
result = vibecount("strawberry", "r")
print(result)  # 3

# Case-insensitive counting
result = vibecount("Strawberry", "R", case_sensitive=False)
print(result)  # 3

# Case-sensitive counting (explicit)
result = vibecount("Strawberry", "R", case_sensitive=True)
print(result)  # 0 (no uppercase 'R' in "Strawberry")
```

### Parameters

- `text` (str): The input string to analyze
- `target_letter` (str): The letter to count (must be a single character)
- `case_sensitive` (bool, optional): Whether to perform case-sensitive counting (default: True)

### Return Value

Returns an integer representing the count of the target letter in the text.

### Error Handling

The function raises:
- `ValueError`: If OpenAI API key is not set or target_letter is not a single character
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
pytest --cov=vibecount
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

This package uses the OpenAI API for letter counting, which requires an API key and internet connection. Each function call will make a request to OpenAI's servers and will consume API credits.
