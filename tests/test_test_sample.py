import pytest

def test_add_positive_numbers():
    assert add(2, 3) == 5
    
def test_add_negative_numbers():
    assert add(-2, -3) == -5
    
def test_add_mixed_numbers():
    assert add(5, -3) == 2
    
def test_add_zero():
    assert add(0, 0) == 0