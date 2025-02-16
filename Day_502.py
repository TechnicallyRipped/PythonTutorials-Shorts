

class Shape():
    def is_shape(self):
        print('I am a shape!')

class Color():
    def call_color(self):
        print('I am blue!')

class Square(Shape,Color):
    def side_count(self):
        print('I have 4 sides!')


x = Square()
x.side_count()
x.is_shape()
x.call_color()



