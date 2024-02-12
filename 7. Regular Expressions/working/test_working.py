import pytest
from working import convert

def main():
    test_wrong_fromat()
    test_time()
    test_hour()
    test_minute()

def test_wrong_fromat():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_hour():
    with pytest.raises(ValueError):
        convert("15 PM to 8 AM")

def test_minute():
    with pytest.raises(ValueError):
        convert("9:70 AM to 5:62 PM")


if __name__ == "__main__":
    main()