# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math
# com essa lib, a dificuldade do problema cai em 90%

resposta = 1
for i in range(1, 21):
    resposta *= i // math.gcd(i, resposta)

print(resposta)
