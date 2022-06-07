import sys

N, M = map(int, input().split())

unheard = set([sys.stdin.readline().rstrip() for _ in range(N)])
unseen = set([sys.stdin.readline().rstrip() for _ in range(M)])

dbj = sorted(list(unheard & unseen))
print(len(dbj))
print(*dbj, sep = "\n")