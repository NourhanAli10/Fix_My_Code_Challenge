#!/usr/bin/python3
"""module for Square class"""


class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ function to Instantiate of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ function to find area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """function to Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print objects in string format"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
