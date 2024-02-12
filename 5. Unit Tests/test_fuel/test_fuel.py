from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_zero_division()
    test_value()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
         convert('cat/fan')

def test_input():
    assert convert('1/2') == 50
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(75) == '75%'


if __name__ == "__main__":
    main()