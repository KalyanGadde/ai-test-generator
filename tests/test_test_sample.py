Here are some unit tests for the given code using pytest:

```python
import pytest
from code_file import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_and_negative_numbers():
    assert add(5, -3) == 2

def test_add_large_numbers():
    assert add(1000, 2000) == 3000
```

Make sure to replace `code_file` with the name of the Python file where your `add` function is defined.