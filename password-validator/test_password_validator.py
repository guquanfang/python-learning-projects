from password_validator import is_valid_password
import pytest

def test_valid_password():
    assert is_valid_password("Hello123")
    assert is_valid_password("Hello6666666666666")

def test_short_password():
    assert not is_valid_password("Hel12 ") 

def test_missing_uppercase():
    assert not is_valid_password("hello123")    

def test_missing_lowercase():
    assert not is_valid_password("HELLO123") 

def test_missing_digit():
    assert not is_valid_password("HelloABC")

def test_toolong_password():
    assert not is_valid_password("Aa66666666666666666666666666666666")

def  test_empty_password():
    assert not is_valid_password("")

def test_special_characters():
    assert is_valid_password("Hello@123")

def test_invalid_type():
    with pytest.raises(TypeError):
        is_valid_password(None)

    with pytest.raises(TypeError):
        is_valid_password(12345678)
