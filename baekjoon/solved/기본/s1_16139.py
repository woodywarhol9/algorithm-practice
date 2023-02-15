import sys
import string

s = input()
q = int(input())
# 알파벳별 저장
char_list = {}
for char in string.ascii_lowercase:
    char_list[char] = [0]
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        char_list[char].append(count)
        
for _ in range(q):
    char, start, end = sys.stdin.readline().rstrip().split()
    start, end = int(start), int(end)
    print(char_list[char][end + 1] - char_list[char][start])