



numbers = [1, 2, 3, 4, 5, 6, 7]

half = len(numbers) // 2

# print(half)

swapped = numbers[half:] + numbers[:half]

print(swapped)