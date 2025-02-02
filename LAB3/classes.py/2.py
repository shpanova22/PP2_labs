class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length )  

class Shape(Square):
    def __init__(self, length = 0 ):
       super().__init__(length)

p = Shape(int(input()))
p.area()
