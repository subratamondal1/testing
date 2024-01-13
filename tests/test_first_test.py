from decimal import DivisionByZero
import pytest
import src.first_test as first_test

def test_add():
    result=first_test.add(a=5, b=6)
    assert result==11

def test_divide():
    result=first_test.divide(a=10, b=5)
    assert result==2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        first_test.divide(a=10, b=0)
