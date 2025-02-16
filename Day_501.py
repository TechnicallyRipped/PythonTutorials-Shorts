

class Shape():
    def is_shape(self):
        print('I am a shape!')

class Square(Shape):
    def side_count(self):
        print('I have 4 sides!')


x = Shape()
x.side_count()
x.is_shape()




