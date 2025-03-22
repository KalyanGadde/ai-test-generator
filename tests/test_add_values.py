def test_add():
    from add_values import add
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2