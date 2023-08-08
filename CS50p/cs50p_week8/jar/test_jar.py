from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"



def test_deposit():
    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.withdraw(10)

