from working import convert
import pytest


def test_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5 PM")
        convert("9 AM - 5:30 PM")
        convert("9 AM - 5 PM")
        convert("9 AM")


def test_hr_valid():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("9 AM to 13 PM")


def test_min_valid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
        convert("9 AM to 5:60 PM")


def test_conversion():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("9:30 AM to 11:59 PM") == "09:30 to 23:59"



