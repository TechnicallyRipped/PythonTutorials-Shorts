

# pip install scipy
from scipy.stats import linregress

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

lin_re = linregress(x, y)

print("slope:", lin_re.slope)
print("intercept:", lin_re.intercept)
print("r-value:", lin_re.rvalue)
print("p-value:", lin_re.pvalue)
print("standard error (slope):", lin_re.stderr)
print("standard error (intercept):", lin_re.intercept_stderr)