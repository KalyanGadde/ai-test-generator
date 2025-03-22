from multiply import multiply

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6
    assert multiply(5, 5) == 25

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-5, -5) == 25

def test_multiply_zero():
    assert multiply(0, 10) == 0
    assert multiply(5, 0) == 0