from twttr import shorten


def test_lower():
    assert shorten("banana") == "bnn"
    assert shorten("twtter") == "twttr"
    assert shorten("big") == "bg"
    assert shorten("world") == "wrld"
    assert shorten("up") == "p"



def test_upper():
    assert shorten("bAnAnA") == "bnn"
    assert shorten("twttEr") == "twttr"
    assert shorten("bIg") == "bg"
    assert shorten("wOrld") == "wrld"
    assert shorten("Up") == "p"


def test_digit():
    assert shorten("FIFA2023") == "FF2023"


def test_punctuation():
    assert shorten("hello!") == "hll!"


def test_print():
    assert shorten("Hello") == "Hll"