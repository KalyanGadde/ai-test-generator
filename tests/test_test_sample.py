```python
import pytest
from mymodule.myfile import add

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_positive_and_negative_numbers():
    assert add(10, -5) == 5

def test_add_zero_and_positive_number():
    assert add(0, 10) == 10

def test_add_zero_and_negative_number():
    assert add(0, -5) == -5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_float_numbers():
    assert add(1.5, 2.5) == 4

def test_add_strings():
    with pytest.raises(TypeError):
        add('hello', 'world')
```