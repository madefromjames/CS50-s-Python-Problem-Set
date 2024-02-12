from seasons import birthday

def main():
    test_correct()


def test_correct():
    assert birthday("2023-02-06") == ('2023', '02', '06')
    assert birthday("2010-4-6") == None
    assert birthday("2024 July 16") == None


if __name__ == "__main__":
    main()