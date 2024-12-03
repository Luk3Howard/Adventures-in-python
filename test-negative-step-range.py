numbers = [1, 3, 5, 8, 10]
max_odd = 0

for x in numbers:
    if x % 2 == 1 and x > max_odd:
        max_odd = x
print(max_odd)