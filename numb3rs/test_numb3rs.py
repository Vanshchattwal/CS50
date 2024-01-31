import pytest
import numb3rs


def main():
    test_nnumbers()
    test_bnumbers()
    test_numbers()


def test_nnumbers():
    assert numb3rs.validate("192.165.-56.12") == False
    assert numb3rs.validate("-192.165.56.12") == False
    assert numb3rs.validate("192.-165.56.12") == False


def test_bnumbers():
    assert numb3rs.validate("192.165.266.12") == False
    assert numb3rs.validate("192.265.66.12") == False
    assert numb3rs.validate("192.165.66.512") == False


def test_numbers():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("192.168.255.1") == True
    assert numb3rs.validate("255.255.255.255") == True


if __name__ == "__main__":
    main()
