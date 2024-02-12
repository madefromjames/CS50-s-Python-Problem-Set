from bank import value

def main():
    test_value_zero()
    test_value_twenty()
    test_value_hundred()
    # value_insensitivity()

def test_value_zero():
    assert value('hello') == 0
    assert value('Hello james') == 0

def test_value_twenty():
    assert value('h') == 20
    assert value('HEY') == 20

def test_value_hundred():
    assert value('What\'s UP') == 100


if __name__ == "__main__":
    main()