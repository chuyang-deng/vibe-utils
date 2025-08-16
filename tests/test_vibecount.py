"""
Tests for vibeutils package
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from vibeutils import vibecount, vibecompare


class TestVibecount:
    """Test cases for the vibecount function"""
    
    def setup_method(self):
        """Set up test environment"""
        # Mock the OpenAI API key for tests
        os.environ["OPENAI_API_KEY"] = "test-api-key"
    
    def teardown_method(self):
        """Clean up test environment"""
        # Remove the test API key
        if "OPENAI_API_KEY" in os.environ:
            del os.environ["OPENAI_API_KEY"]
    
    def test_missing_api_key(self):
        """Test that ValueError is raised when API key is missing"""
        del os.environ["OPENAI_API_KEY"]
        
        with pytest.raises(ValueError, match="OPENAI_API_KEY environment variable is not set"):
            vibecount("test", "t")
    
    def test_invalid_target_letter_empty(self):
        """Test that ValueError is raised for empty target letter"""
        with pytest.raises(ValueError, match="target_letter must be a single character"):
            vibecount("test", "")
    
    def test_invalid_target_letter_multiple(self):
        """Test that ValueError is raised for multiple character target letter"""
        with pytest.raises(ValueError, match="target_letter must be a single character"):
            vibecount("test", "ab")
    
    def test_invalid_target_letter_non_string(self):
        """Test that ValueError is raised for non-string target letter"""
        with pytest.raises(ValueError, match="target_letter must be a single character"):
            vibecount("test", 123)
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_successful_case_sensitive_count(self, mock_openai):
        """Test successful case-sensitive letter counting"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "3"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecount("strawberry", "r", case_sensitive=True)
        
        assert result == 3
        mock_client.chat.completions.create.assert_called_once()
        
        # Verify the API call parameters
        call_args = mock_client.chat.completions.create.call_args
        assert call_args[1]["model"] == "gpt-4o-mini"
        assert call_args[1]["max_tokens"] == 10
        assert call_args[1]["temperature"] == 0
        assert "case-sensitive" in call_args[1]["messages"][0]["content"]
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_successful_case_insensitive_count(self, mock_openai):
        """Test successful case-insensitive letter counting"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "4"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecount("Strawberry", "r", case_sensitive=False)
        
        assert result == 4
        mock_client.chat.completions.create.assert_called_once()
        
        # Verify case-insensitive instruction is in the prompt
        call_args = mock_client.chat.completions.create.call_args
        assert "case-insensitive" in call_args[1]["messages"][0]["content"]
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_default_case_sensitive(self, mock_openai):
        """Test that case_sensitive defaults to True"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "2"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecount("test", "t")  # Not specifying case_sensitive
        
        assert result == 2
        
        # Verify case-sensitive instruction is in the prompt (default behavior)
        call_args = mock_client.chat.completions.create.call_args
        assert "case-sensitive" in call_args[1]["messages"][0]["content"]
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_openai_api_failure(self, mock_openai):
        """Test handling of OpenAI API failures"""
        # Mock the OpenAI client to raise an exception
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        with pytest.raises(Exception, match="OpenAI API call failed: API Error"):
            vibecount("test", "t")
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_unexpected_openai_response(self, mock_openai):
        """Test handling of unexpected OpenAI responses"""
        # Mock the OpenAI response with non-integer content
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "not a number"
        mock_client.chat.completions.create.return_value = mock_response
        
        with pytest.raises(Exception, match="OpenAI API returned unexpected response"):
            vibecount("test", "t")
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_empty_text(self, mock_openai):
        """Test counting letters in empty text"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "0"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecount("", "a")
        
        assert result == 0
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_zero_count(self, mock_openai):
        """Test when letter is not found in text"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "0"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecount("hello", "z")
        
        assert result == 0
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_prompt_content(self, mock_openai):
        """Test that the prompt contains expected elements"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "1"
        mock_client.chat.completions.create.return_value = mock_response
        
        vibecount("hello", "h", case_sensitive=True)
        
        # Verify the prompt structure
        call_args = mock_client.chat.completions.create.call_args
        prompt = call_args[1]["messages"][0]["content"]
        
        assert "Count how many times the letter 'h' appears" in prompt
        assert "hello" in prompt
        assert "case-sensitive" in prompt
        assert "Only return the number as your response" in prompt


class TestVibecompare:
    """Test cases for the vibecompare function"""
    
    def setup_method(self):
        """Set up test environment"""
        # Mock the OpenAI API key for tests
        os.environ["OPENAI_API_KEY"] = "test-api-key"
    
    def teardown_method(self):
        """Clean up test environment"""
        # Remove the test API key
        if "OPENAI_API_KEY" in os.environ:
            del os.environ["OPENAI_API_KEY"]
    
    def test_missing_api_key(self):
        """Test that ValueError is raised when API key is missing"""
        del os.environ["OPENAI_API_KEY"]
        
        with pytest.raises(ValueError, match="OPENAI_API_KEY environment variable is not set"):
            vibecompare(5, 10)
    
    def test_invalid_first_argument(self):
        """Test that ValueError is raised for non-numeric first argument"""
        with pytest.raises(ValueError, match="Both arguments must be numbers"):
            vibecompare("5", 10)
    
    def test_invalid_second_argument(self):
        """Test that ValueError is raised for non-numeric second argument"""
        with pytest.raises(ValueError, match="Both arguments must be numbers"):
            vibecompare(5, "10")
    
    def test_invalid_both_arguments(self):
        """Test that ValueError is raised for non-numeric arguments"""
        with pytest.raises(ValueError, match="Both arguments must be numbers"):
            vibecompare("5", "10")
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_first_number_smaller(self, mock_openai):
        """Test comparison when first number is smaller"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "-1"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(5, 10)
        
        assert result == -1
        mock_client.chat.completions.create.assert_called_once()
        
        # Verify the API call parameters
        call_args = mock_client.chat.completions.create.call_args
        assert call_args[1]["model"] == "gpt-4o-mini"
        assert call_args[1]["max_tokens"] == 10
        assert call_args[1]["temperature"] == 0
        assert "5" in call_args[1]["messages"][0]["content"]
        assert "10" in call_args[1]["messages"][0]["content"]
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_numbers_equal(self, mock_openai):
        """Test comparison when numbers are equal"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "0"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(7, 7)
        
        assert result == 0
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_first_number_larger(self, mock_openai):
        """Test comparison when first number is larger"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "1"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(15, 8)
        
        assert result == 1
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_float_numbers(self, mock_openai):
        """Test comparison with float numbers"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "-1"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(3.14, 3.15)
        
        assert result == -1
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_mixed_int_float(self, mock_openai):
        """Test comparison with mixed int and float"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "1"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(5, 4.9)
        
        assert result == 1
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_openai_api_failure(self, mock_openai):
        """Test handling of OpenAI API failures"""
        # Mock the OpenAI client to raise an exception
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        
        with pytest.raises(Exception, match="OpenAI API call failed: API Error"):
            vibecompare(5, 10)
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_unexpected_openai_response(self, mock_openai):
        """Test handling of unexpected OpenAI responses"""
        # Mock the OpenAI response with non-integer content
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "not a number"
        mock_client.chat.completions.create.return_value = mock_response
        
        with pytest.raises(Exception, match="OpenAI API returned unexpected response"):
            vibecompare(5, 10)
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_invalid_comparison_result(self, mock_openai):
        """Test handling of invalid comparison results"""
        # Mock the OpenAI response with invalid comparison result
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "2"  # Invalid result
        mock_client.chat.completions.create.return_value = mock_response
        
        with pytest.raises(Exception, match="OpenAI API returned invalid comparison result"):
            vibecompare(5, 10)
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_negative_numbers(self, mock_openai):
        """Test comparison with negative numbers"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "1"
        mock_client.chat.completions.create.return_value = mock_response
        
        result = vibecompare(-5, -10)
        
        assert result == 1
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('vibeutils.core.openai.OpenAI')
    def test_prompt_content(self, mock_openai):
        """Test that the prompt contains expected elements"""
        # Mock the OpenAI response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "-1"
        mock_client.chat.completions.create.return_value = mock_response
        
        vibecompare(3, 7)
        
        # Verify the prompt structure
        call_args = mock_client.chat.completions.create.call_args
        prompt = call_args[1]["messages"][0]["content"]
        
        assert "Compare the two numbers 3 and 7" in prompt
        assert "-1 if the first number" in prompt
        assert "0 if the numbers are equal" in prompt
        assert "1 if the first number" in prompt
        assert "Only return the number (-1, 0, or 1)" in prompt
