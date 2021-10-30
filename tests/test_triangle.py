import pytest
from src.triangle import Triangle

def test_01():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == 6


def test_02():
    triangle = Triangle(2, 2, 2)
    print(triangle.perimeter)
    assert triangle.perimeter == 6


@pytest.mark.xfail(raises=(ValueError))
def test_fail_exception():
    triangle = Triangle(5, 2, 2)
    raise ValueError

def test_04():
    triangle_1 = Triangle(3, 4, 5)
    triangle_2 = Triangle(5, 12, 13)
    assert triangle_1 + triangle_2 == 36

@pytest.mark.xfail(raises=(ValueError))
def test_05():
    triangle_1 = Triangle(1, 3, 3)
    assert triangle_1 + "abc" == 10
