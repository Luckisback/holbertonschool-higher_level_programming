#!/usr/bin/python3
"""
Base Class
Args:
    Base: First class
    __nb_objects: the private class attribut
    id: A public instance attribut
    Rectangle: A classe inherite the classe Base
    __width, __height, __x, __y: Private instance attribute of Rectangle
    area: Public methode that returns the   rea value of the rectangle
    update: The method that assigns an argument to each attribute
"""


class Base:
    """ The first class called base """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """ A classe inherite Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialisation of the instances"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Setting of the Rectangle's instance attribute behaviors
    @property
    def width(self):
        """ definition of width as an object's property"""
        return self.__width

    @width.setter
    def width(self, value):
        """ definition of, How width should act"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ definition of height as an object's property"""
        return self.__height

    @height.setter
    def height(self, value):
        """ definition of, How height should act"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ definition of 'x' as an object's property"""
        return self.__x

    @x.setter
    def x(self, value):
        """ definition of, How 'x' should act"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ definition of 'y' as an object's property"""
        return self.__y

    @y.setter
    def y(self, value):
        """ definition of, How 'y' should act"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Adding of the public method area"""
    def area(self):
        """The method that returns the area  value of Rectangle"""
        return self.__width * self.height

    """Adding of the public method display"""
    def display(self):
        """ Printing '#' carracters => value of width and height"""
        """seconde time: taking care of 'x' and 'y' before printing"""
        absices = self.__x * " "
        ordonnés = self.__y
        for i in range(ordonnés):
            print('')
        for i in range(self.height):
            print("{}".format(absices), end="")
            for i in range(self.width):
                print("{}".format("#"), end='')
            print("")

    """Adding of the method __str__ for a specific display"""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    """Updating of the class Rectangle, by the adding of the method update"""

    def update(self, *args, **kwargs):
        """The method that assigns an argument to each attribute"""
        """Seonde time, update the code by adding **kargs parameter"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

