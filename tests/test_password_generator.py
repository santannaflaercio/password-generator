import pytest
from password_generator import generate_password
from unittest.mock import patch


@patch("json.load")
def test_default_password_characters(mock_json_load):
    mock_json_load.return_value = {
        "password_length": 6,
        "default_characters": "abc",
        "specific_requirements": {
            "digits": False,
            "symbols": False,
        },
    }
    result = generate_password()
    assert all(char in "abc" for char in result)


@patch("json.load")
def test_password_with_digits(mock_json_load):
    mock_json_load.return_value = {
        "default_characters": "abc",
        "allowed_digits": "0123456789",
        "password_length": 10,
        "specific_requirements": {
            "digits": True,
            "symbols": False,
        },
    }

    result = generate_password()
    assert any(char in "0123456789" for char in result)


@patch("json.load")
def test_password_with_symbols(mock_json_load):
    mock_json_load.return_value = {
        "default_characters": "abc",
        "allowed_symbols": "!@#$%^",
        "password_length": 10,
        "specific_requirements": {
            "digits": False,
            "symbols": True,
        },
    }

    result = generate_password()
    assert any(char in "!@#$%^" for char in result)


@patch("json.load")
def test_password_with_digits_and_symbols(mock_json_load):
    mock_json_load.return_value = {
        "default_characters": "abc",
        "allowed_digits": "012345",
        "allowed_symbols": "!@#$%^",
        "password_length": 10,
        "specific_requirements": {
            "digits": True,
            "symbols": True,
        },
    }

    result = generate_password()
    assert any(char in "!@#$%^012345" for char in result)
