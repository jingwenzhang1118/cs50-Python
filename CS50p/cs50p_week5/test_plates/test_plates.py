from plates import is_valid


def test_len():
    assert is_valid("A") == False
    assert is_valid("ABCDE") == True
    assert is_valid("ABCDEFG") == False


def test_first2char():
    assert is_valid("A3") == False
    assert is_valid("3A") == False

def test_digits():
    assert is_valid("ABC02") == False
    assert is_valid("ABC33A") == False


def test_otherchar():
    assert is_valid("AB,D") == False
    assert is_valid("AB-D") == False