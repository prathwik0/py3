#power of a number with and without built in functions
import math

base = 2
x = 5

pwr = 1

for i in range(x):
    pwr = pwr * base

print("a^b without built in functions is", pwr)

print("a^b using built in func. is", pow(base,x))
