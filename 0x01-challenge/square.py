#!/usr/bin/python3
"""
Square class
"""


class Square:
    def __init__(self, width=0, height=0, *args, **kwargs):
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(f"Area: {s.area_of_my_square()}")
    print(f"Perimeter: {s.perimeter_of_my_square()}")
