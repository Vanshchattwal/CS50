from um import count
import pytest


def main():
    tests()


def tests():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("hello, world !") == 0


if __name__ == "__main__":
    main()
