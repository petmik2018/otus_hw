import pytest
from src.square import Square

def test_01():
    figure = Square(2)
    assert figure.area == 4


def test_02():
    figure = Square(2)
    print(figure.perimeter)
    assert figure.perimeter == 8