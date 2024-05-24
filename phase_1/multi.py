# product of two numbers without using *

a = int(input())
b = int(input())
"""
print(a//(1/b))
"""
sum = 0
for i in range(a):
    sum += b
print(sum)