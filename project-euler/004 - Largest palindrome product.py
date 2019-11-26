# Find the largest palindrome made from the product of two 3-digit numbers.
# A palindromic number reads the same both ways


def three_digits_palindome():
    answer = max(i * j
                 for i in range(100, 1000)
                 for j in range(100, 1000)
                 if str(i * j) == str(i * j)[:: -1])
    return str(answer)


print(three_digits_palindome())
