

def my_decorator(og):
    def wrapper():
        print('Running OG function')
        og()
        print('Done running OG function')
    return wrapper


@my_decorator
def bark():
    print('WOOF!')


bark()


























