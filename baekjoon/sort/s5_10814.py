import sys

n = int(input())
member_info = []
for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    member_info.append([age, name])

member_info.sort(key = lambda x : (x[0]))
for a, b in member_info:
    print(a, b)