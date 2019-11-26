even_numbers = 0
# first two terms | x = current Fibonacci number, y = the next Fibonacci number
x, y = 1, 2
while x < 4000000:
    if (x % 2 == 0):
        even_numbers += x
    x, y = y, x + y
print(even_numbers)
