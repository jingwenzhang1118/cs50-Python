from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_h():
    assert value("how are you?") == 20


def test_other():
    assert value("What a nice day!") == 100


def test_otherchar():
    assert value("123") == 100
    assert value("!") == 100

