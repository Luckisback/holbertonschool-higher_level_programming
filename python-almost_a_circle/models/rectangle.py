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
        super().__init__(id)

        self.__width = width
        self.__height = height
        __x = x
        __y = y

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
        
    #Adding of the public method area
    
    def area(self):
        """The method that returns the area  avlue of Rectangle"""
        return self.__width * self.height
    
    #Adding of the public method display
    
    def display(self):
        """ The methode that print '#' carracter corresponding to value of width and height"""
        for i in range(self.height):
            for i in range(self.width):
                print("{}".format("#"), end='')
            print("")
            
    #Adding of the method __str__ for a specific display
        
    def __str__(self):
        """ this method return a particular display: [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)