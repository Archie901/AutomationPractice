import pytest
from cards import Card

def test_with_fail():
    c1 = Card("sit here", "brian")
    c2 = Card("do anyth", "okken")
    if c1 != c2:
        pytest.fail("THEY DO NOT MACTH!")