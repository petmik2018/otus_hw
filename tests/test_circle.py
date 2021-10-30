import pytest
import math
from src.circle import Circle

def test_01():
    figure = Circle(1)
    assert figure.area == math.pi


def test_02():
    figure = Circle(1)
    print(figure.perimeter)
    assert figure.perimeter == 2 * math.pi