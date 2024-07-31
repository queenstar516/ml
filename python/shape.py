from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def getWidth(self):
        return self.width
    
    def getLength(self):
        return self.length
