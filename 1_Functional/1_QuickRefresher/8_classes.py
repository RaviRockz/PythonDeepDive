class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __str__(self):
        return 'Rectangle\n\t--> Width  :: {0}\n\t--> Height :: {1}'.format(self.__width, self.__height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width) * (2 * self.__height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.__width is other.__width) and (self.__height is other.__height)
        else:
            raise TypeError('{0} is not a type of {1}'.format(other, Rectangle))

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError('{0} is not a type of {1}'.format(other, Rectangle))

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            raise TypeError('{0} is not a type of {1}'.format(other, Rectangle))

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, width):
        if width <=0:
            raise ValueError('Width Of Rectangle Must Be Positive')
        else:
            self.__width = width
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height Of Rectangle Must Be Positive')
        else:
            self.__height = height
            

rect = Rectangle(10, 20)
print(rect)
print(repr(rect))
print(rect.area())
print(rect.perimeter())

rect.width = 15
rect.height = 15

print(rect.width)
print(rect.height)

rect1 = Rectangle(10, 20)
rect2 = Rectangle(10, 30)
print(rect == rect1)
print(rect == rect2)
print(rect < rect1)
print(rect < rect2)
print(rect > rect1)
print(rect > rect2)
