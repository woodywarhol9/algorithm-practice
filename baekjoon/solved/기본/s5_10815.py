import sys

N = int(input())
card = set(sys.stdin.readline().rstrip().split())

M = int(input())
check = sys.stdin.readline().rstrip().split()
check = [1 if i in card else 0 for i in check]
print(*check)
