from shape import Shape

class Triangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)
    
    def area(self):
        return (1/2) * (self.length * self.width)
    
    def perimeter(self):
        return self.length + self.width