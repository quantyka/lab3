class Shape:
    def __init__(self, a=0):  
        self.a = a

    def area(self):
        return 0 


class Square(Shape):
    def __init__(self, length):
        super().__init__(length) 
        self.length = length 

    def area(self):
        return self.length ** 2  


shape = Shape()
print(f"Площадь фигуры (Shape): {shape.area()}")  


a = int(input())
square = Square(a)
print(f"Площадь квадрата (Square) со стороной {a}: {square.area()}")