import sys

A, B = map(int, input().split())

A_set = set(sys.stdin.readline().rstrip().split())
B_set = set(sys.stdin.readline().rstrip().split())

print(len(list((A_set-B_set)|(B_set-A_set))))