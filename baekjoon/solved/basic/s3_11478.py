S = input()
word = set()
for i in range(1, len(S) + 1):
    for j in range(0, len(S)):
        if j + i > len(S): # j가 남아 실행되는 것 방지
            break
        word.add(S[j : j + i])
print(len(word))