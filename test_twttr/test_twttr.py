from twttr import shorten


def main():
    test_vowels()


def test_vowels():
    assert shorten("aeiouff") == "ff"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWITTER45") == "TWTTR45"
    assert shorten("TWITTER!") == "TWTTR!"


if __name__ == "__main__":
    main()
