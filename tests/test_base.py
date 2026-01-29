import pytest
import math
from base import (
    Point, Vector, translate, rotate, 
    scale, reflect, distance, midpoint
)


class TestPoint:
    def test_point_creation(self):
        p = Point(3, 4)
        assert p.x == 3
        assert p.y == 4
    
    def test_point_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(1, 2.0000001)
        assert p1 == p2
        assert p1 != p3


class TestVector:
    def test_vector_creation(self):
        v = Vector(2, 3)
        assert v.x == 2
        assert v.y == 3
    
    def test_vector_from_points(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        v = Vector.from_points(p1, p2)
        assert v.x == 3
        assert v.y == 4


class TestTranslate:
    def test_translate_point(self):
        p = Point(1, 2)
        v = Vector(3, 4)
        result = translate(p, v)
        assert result == Point(4, 6)


class TestRotate:
    def test_rotate_around_origin(self):
        p = Point(1, 0)
        result = rotate(p, 90)
        assert math.isclose(result.x, 0, abs_tol=1e-10)
        assert math.isclose(result.y, 1, abs_tol=1e-10)
    
    def test_rotate_around_point(self):
        p = Point(2, 0)
        center = Point(1, 0)
        result = rotate(p, 90, center)
        assert math.isclose(result.x, 1, abs_tol=1e-10)
        assert math.isclose(result.y, 1, abs_tol=1e-10)


class TestScale:
    def test_scale_from_origin(self):
        p = Point(2, 3)
        result = scale(p, 2)
        assert result == Point(4, 6)
    
    def test_scale_from_point(self):
        p = Point(3, 4)
        center = Point(1, 1)
        result = scale(p, 2, center)
        assert result == Point(5, 7)


class TestReflect:
    def test_reflect_x(self):
        p = Point(2, 3)
        result = reflect(p, 'x')
        assert result == Point(2, -3)
    
    def test_reflect_y(self):
        p = Point(2, 3)
        result = reflect(p, 'y')
        assert result == Point(-2, 3)
    
    def test_reflect_invalid_axis(self):
        p = Point(2, 3)
        with pytest.raises(ValueError):
            reflect(p, 'z')


class TestDistance:
    def test_distance_between_points(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        assert distance(p1, p2) == 5


class TestMidpoint:
    def test_midpoint(self):
        p1 = Point(0, 0)
        p2 = Point(4, 6)
        result = midpoint(p1, p2)
        assert result == Point(2, 3)


def test_all_operations_chain():
    p = Point(1, 1)
    
    p = translate(p, Vector(2, 1))  # (3, 2)
    
    p = rotate(p, 90)  # (-2, 3)
    
    p = scale(p, 2)  # (-4, 6)
    
    p = reflect(p, 'x')  # (-4, -6)
    
    assert math.isclose(p.x, -4, abs_tol=1e-10)
    assert math.isclose(p.y, -6, abs_tol=1e-10)