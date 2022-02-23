"""
replace 함수 사용 후 다시 할당해줘야 한다!
"""

croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

word = input()

for i in croatia_alphabet:
    if i in word:
        word = word.replace(i, "0")

print(len(word))
