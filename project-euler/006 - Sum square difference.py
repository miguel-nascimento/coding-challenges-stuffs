# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def diffence_sum_squares():
    s = sum(i for i in range(1, 101))
    s2 = sum(i**2 for i in range(1, 101))
    return str(s**2 - s2)


print(diffence_sum_squares())
