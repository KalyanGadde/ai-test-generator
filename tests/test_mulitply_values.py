from multiply_values import multiply

def test_multiply_positive_numbers():
    assert multiply(3, 5) == 15

def test_multiply_negative_numbers():
    assert multiply(-4, 7) == -28

def test_multiply_zero():
    assert multiply(6, 0) == 0