"""
Минимальная геометрическая библиотека для трансформаций.
"""

import math
from typing import Tuple


class Point:
    """Точка в 2D пространстве."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)


class Vector:
    """Вектор в 2D пространстве."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> 'Vector':
        """Создать вектор из двух точек."""
        return cls(p2.x - p1.x, p2.y - p1.y)


def translate(point: Point, vector: Vector) -> Point:
    """Переместить точку на вектор."""
    return Point(point.x + vector.x, point.y + vector.y)


def rotate(point: Point, angle_degrees: float, center: Point = None) -> Point:
    """
    Повернуть точку на угол вокруг центра.
    Если центр не указан, поворот вокруг начала координат.
    """
    if center is None:
        center = Point(0, 0)
    
    # Перемещаем точку в систему координат с центром в центре вращения
    dx = point.x - center.x
    dy = point.y - center.y
    
    # Преобразуем градусы в радианы
    angle_rad = math.radians(angle_degrees)
    
    # Поворачиваем
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    
    new_x = dx * cos_a - dy * sin_a
    new_y = dx * sin_a + dy * cos_a
    
    # Возвращаем в исходную систему координат
    return Point(new_x + center.x, new_y + center.y)


def scale(point: Point, factor: float, center: Point = None) -> Point:
    """
    Масштабировать точку относительно центра.
    Если центр не указан, масштабирование относительно начала координат.
    """
    if center is None:
        center = Point(0, 0)
    
    dx = point.x - center.x
    dy = point.y - center.y
    
    new_x = center.x + dx * factor
    new_y = center.y + dy * factor
    
    return Point(new_x, new_y)


def reflect(point: Point, axis: str = 'x') -> Point:
    """
    Отразить точку относительно оси.
    
    Args:
        point: Исходная точка
        axis: 'x' для отражения по оси X, 'y' для отражения по оси Y
    
    Returns:
        Новая отраженная точка
    """
    if axis == 'x':
        return Point(point.x, -point.y)
    elif axis == 'y':
        return Point(-point.x, point.y)
    else:
        raise ValueError("axis должен быть 'x' или 'y'")


def distance(p1: Point, p2: Point) -> float:
    """Вычислить расстояние между двумя точками."""
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def midpoint(p1: Point, p2: Point) -> Point:
    """Найти середину между двумя точками."""
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)