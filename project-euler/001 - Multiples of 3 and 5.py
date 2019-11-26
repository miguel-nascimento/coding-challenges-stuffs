i = 0
total = 0
while (i < 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i
    i += 1
print(total)
# total = 233168 -> sum of all multiples of 3 or 5 below 1000
