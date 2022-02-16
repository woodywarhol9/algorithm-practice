#string에 미리 정의된 상수 이용하기
import string

S = input()
alphabet_check = dict(zip(string.ascii_lowercase, [-1] * 26))

for idx, char in enumerate(S):
    if char in alphabet_check and alphabet_check[char] == -1:
        alphabet_check[char] = idx
print(*alphabet_check.values())

