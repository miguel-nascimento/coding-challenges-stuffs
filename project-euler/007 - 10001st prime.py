# method of Sieve of Eratosthenes
import math


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


counter = 2
num = 3

while counter <= 10001:
    if is_prime(num):
        counter += 1
        num += 2
    else:
        num += 2

print(num - 2)  # 104743
