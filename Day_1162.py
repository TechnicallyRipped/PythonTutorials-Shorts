

class Guy():
    def __init__(self, name):
        self.name = name

    def __iadd__(self, text):
        self.name = text
        return self 


x = Guy('Joe')
x += 'Mike'

print(x.name)
