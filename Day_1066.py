



nums = [1,2,3,4,5,6,7,8,9,10]

count = 0

for i in nums:
    if i > 5:
        count += 1

print(count)

count2 = sum(i > 5 for i in nums)

print(count2)
print(sum([False]))