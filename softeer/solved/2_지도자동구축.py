import sys

n = int(input())
length = 2
for i in range(n):
    length += (2 ** i)
print(length ** 2)