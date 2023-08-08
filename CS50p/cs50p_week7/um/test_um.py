from um import count


def test_in_words():
    assert count("yummy") == 0


def test_punc():
    assert count("hello, um") == 1
    assert count("hello, um,") == 1
    assert count("hello, um.") == 1
    assert count("hello, um?") == 1
    assert count("hello, um!") == 1


def test_start():
    assert count("um") == 1
    assert count("um, um...") == 2


def test_space():
    assert count("  um  ") == 1


def test_case():
    assert count("um, uM...Um") == 3

