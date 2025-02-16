


from typing import Any

def tutorial(x:Any):
    if isinstance(x,str):
        print('Str')
    elif isinstance(x,int):
        print('Int')


tutorial()
