from ctypes.wintypes import RECT, POINT

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_wintypes(cls, point: POINT):
        # noinspection PyArgumentList
        return cls(
            point.x,
            point.y,
        )

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return type(self)(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return type(self)(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass
class Rect:
    left: int
    top: int
    right: int
    bottom: int

    @classmethod
    def from_wintypes(cls, rect: RECT):
        # noinspection PyArgumentList
        return cls(
            rect.left,
            rect.top,
            rect.right,
            rect.bottom,
        )

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top

    @property
    def p_left_top(self) -> Point:
        return Point(self.left, self.top)

    @property
    def p_right_top(self) -> Point:
        return Point(self.right, self.top)

    @property
    def p_left_bottom(self) -> Point:
        return Point(self.left, self.bottom)

    @property
    def p_right_bottom(self) -> Point:
        return Point(self.right, self.bottom)
