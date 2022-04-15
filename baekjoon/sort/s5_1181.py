import sys

n = int(input())
char_list = set(sys.stdin.readline().rstrip() for _ in range(n))
char_list = list(char_list)
char_list.sort(key = lambda x : (len(x), x))
print(*char_list, sep ="\n")