"""
S와 U만 따로 뺴주면 나머진 3의 배수로 처리 가능.
"""

word = input()
count = 0

for i in word:
    if ord(i) == 83: #unicode of S
        count += 8
    elif ord(i) == 86: #unicode of v
        count += 9
    else:
        count += (3 + (ord(i) - 65) // 3) #unicode of A

print(count)
    