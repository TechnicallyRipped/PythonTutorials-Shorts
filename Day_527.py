

import ast

x = "{'Hello':'World'}"

# print(x)
# print(type(x))

y = ast.literal_eval(x)
print(y)
print(type(y))





