import sys

N, M = map(int, input().split())
word = set([sys.stdin.readline().rstrip() for _ in range(N)])
check = [sys.stdin.readline().rstrip() for _ in range(M)]
check = [1 for i in check if i in word]
print(sum(check))