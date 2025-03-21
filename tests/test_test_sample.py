from src import add

def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_zero():
    assert add(0, 0) == 0

def test_add_decimal():
    assert add(3.14, 2.86) == 6.0