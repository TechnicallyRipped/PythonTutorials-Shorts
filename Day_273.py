

import timeit

start = timeit.default_timer()

for i in range(10_000_000):
    pass

end = timeit.default_timer()
elapsed_time = round(end - start,4)

print(f"Time: {elapsed_time} seconds")






















