from twttr import shorten

def main():
    shorter()

def test_shorter():
    assert shorten('word') == 'wrd'
    assert shorten('WORD') == 'WRD'
    assert shorten('word24') == 'wrd24'
    assert shorten('dear, word!') == 'dr, wrd!'


if __name__ == "__main__":
    main()