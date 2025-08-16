"""
Pytest configuration and fixtures
"""

import pytest
import os


@pytest.fixture(autouse=True)
def mock_env_vars():
    """Fixture to ensure clean environment for each test"""
    # Store original environment
    original_env = os.environ.copy()
    
    yield
    
    # Restore original environment after test
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_texts():
    """Fixture providing sample texts for testing"""
    return {
        "simple": "hello",
        "repeated": "strawberry", 
        "mixed_case": "Hello World",
        "empty": "",
        "special_chars": "hello, world!",
        "numbers": "abc123def"
    }
