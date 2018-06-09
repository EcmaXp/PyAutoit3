import ctypes
import operator
from ctypes.wintypes import RECT, POINT
from typing import Callable, Union

from dataclasses import dataclass

from pyautoit3.dll.api import AU3_INTDEFAULT


@dataclass(frozen=True)
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

    def __add__(self, other: "Point") -> "Point":
        if isinstance(other, Point):
            return type(self)(
                self.x + other.x,
                self.y + other.y,
            )

        return NotImplemented

    def __sub__(self, other: "Point") -> "Point":
        if isinstance(other, Point):
            return type(self)(
                self.x - other.x,
                self.y - other.y,
            )

        return NotImplemented

    def zero(self) -> "Rect":
        return Rect(
            self.x,
            self.y,
            self.x,
            self.y,
        )

    def to_wintypes(self):
        point = POINT()
        point.x = self.x,
        point.y = self.y
        return point


DEFAULT_POINT = Point(
    x=AU3_INTDEFAULT,
    y=AU3_INTDEFAULT,
)


@dataclass(frozen=True)
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
        return abs(self.right - self.left)

    @property
    def height(self):
        return abs(self.bottom - self.top)

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

    @property
    def range_x(self):
        return range(
            min(self.left, self.right),
            max(self.left, self.right),
        )

    @property
    def range_y(self):
        return range(
            min(self.top, self.top),
            max(self.bottom, self.bottom),
        )

    def _calc(self, other: "Rect", op: Callable[[int, int], int]) -> "Rect":
        return type(self)(
            op(self.left, other.left),
            op(self.top, other.top),
            op(self.right, other.right),
            op(self.bottom, other.bottom),
        )

    def __add__(self, other: "Rect") -> "Rect":
        if isinstance(other, Rect):
            return self._calc(other, operator.add)

        return NotImplemented

    def __sub__(self, other: "Rect") -> "Rect":
        if isinstance(other, Rect):
            return self._calc(other, operator.sub)

        return NotImplemented

    def __contains__(self, obj):
        if isinstance(obj, Point):
            return obj.x in self.range_x and obj.y in self.range_y

        return NotImplemented

    def to_wintypes(self):
        rect = RECT()
        rect.left = self.left
        rect.top = self.top
        rect.right = self.right
        rect.bottom = self.bottom
        return rect
