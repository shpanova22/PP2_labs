class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length )  

class Shape(Square): # shape наследует square. это значить, shape получает все атрибуты и методы(конструктор)
    def __init__(self, length = 0): # по  умолчанию 0
        super().__init__(length) #вызывает конструктор родительского класса Square, передавая length
        
        
p = Shape(int(input()))
p.area()
