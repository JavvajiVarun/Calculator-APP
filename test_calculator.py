from calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2, 3) == 6


def test_subtract():
    assert subtract(10, 2, 3) == 5


def test_multiply():
    assert multiply(2, 3, 4) == 24


def test_divide():
    assert divide(24, 2, 3) == 4