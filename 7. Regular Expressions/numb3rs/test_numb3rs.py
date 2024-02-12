from numb3rs import validate

def main():
    test_ipv4()
    test_range()

def test_ipv4():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"0.2.44.5") == True
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False
    assert validate(r"999.25.44.1") == False
    assert validate(r"100.685.432.289") == False

if __name__ == "__main__":
    main()