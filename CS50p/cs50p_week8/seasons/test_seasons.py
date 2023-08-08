from seasons import check_birth, minutes
import pytest


def test_format():
    assert check_birth("1999-09-01") == "1999-09-01"
    with pytest.raises(SystemExit):
        check_birth("January 1, 1999")
        check_birth("1999-9-1")
        minutes("1999-13-01")

    # with pytest.raises(Exception) for raising exceptions
    # with pytest.raises(Exception) for existing system


def test_calculation():
    assert minutes("2023-02-10") == "One thousand, four hundred forty minutes"

