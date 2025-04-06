

# pip install timeit

from timeit import timeit

total_time = timeit("sum(range(100))",
                    number=1000)

print(total_time)

avg_time = total_time/1000
print(avg_time)

