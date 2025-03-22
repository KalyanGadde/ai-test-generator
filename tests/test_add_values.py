# Contents of test_add_values.py

from add_values import add

def test_add_positive_values():
    assert add(3, 5) == 8

def test_add_negative_values():
    assert add(-3, -5) == -8

def test_add_mixed_values():
    assert add(-3, 5) == 2