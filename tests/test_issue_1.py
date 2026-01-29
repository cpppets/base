import pytest
import math
from base import (
    Point, Vector, translate, rotate, 
    scale, reflect, distance, midpoint
)


class TestPoint:
    
    def test_point_multiplication(self):
        p1 = Point(1, 2)
        p2 = p1 * 2
        p3 = 2 * p1
        assert p2 == p3
        assert p2.x == 2
        assert p2.y == 4

    