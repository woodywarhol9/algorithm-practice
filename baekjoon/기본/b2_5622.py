word = input()
count = 0

for i in word:
    count += (2 + (ord(i) - 65) // 3) #unicode of A

print(count)
    