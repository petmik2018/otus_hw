import pytest
from src.rectangle import Rectangle

def test_01():
    figure = Rectangle(3, 4)
    assert figure.area == 12


def test_02():
    figure = Rectangle(3, 2)
    print(figure.perimeter)
    assert figure.perimeter == 10