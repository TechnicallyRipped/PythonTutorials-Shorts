

from itertools import accumulate
import operator

x = [1,2,3,4,5]

y = list(accumulate(x,func=operator.mul))
print(y)














