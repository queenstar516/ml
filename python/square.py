from shape import Shape

class Square(Shape):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)
    
    def area(self):
        return (1/2) * (self.length**2)
    
    def perimeter(self):
        return 4 * self.length