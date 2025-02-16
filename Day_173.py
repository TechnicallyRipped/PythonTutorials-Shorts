



# pip install sympy

import sympy as sp

x = sp.symbols('x')

f = x**2

f_prime = sp.diff(f, x)

print(f_prime)

x_3 = f_prime.subs(x, 3)

print(x_3)




























