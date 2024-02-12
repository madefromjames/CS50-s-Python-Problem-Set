from plates import is_valid
def main():
    test_plates_valid()
    test_plates_invalid()


def test_plates_valid():
    assert is_valid('CS50') == True
    assert is_valid('AAA222') == True
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True

def test_plates_invalid():
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('CS05') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('12345') == False


if __name__ == "__main__":
    main()