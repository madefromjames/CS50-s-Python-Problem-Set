from um import count

def main():
    test_um()


def test_um():
    assert count("This is, um... CS50.") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Hello, world") == 0
    assert count("Hello um world") == 1
    assert count("Um... what are regular expressions?") != 0
    assert count("yummy") == 0


if __name__ == "__main__":
    main()