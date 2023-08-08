import pytest
from fuel import convert, gauge

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_ValueError():
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("0")


def test_frac():
    assert convert("2/3") == 67
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"