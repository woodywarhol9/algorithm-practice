"""
가능하면 str 내장함수로 풀어보자.
"""


N = int(input())
count = 0

for i in range(N):
    word = input()
    char_set = set(word)
    for c in char_set:
        if word.count(c) != (word.rfind(c) - word.find(c) + 1):
            break   
    else:
        count += 1

print(count)
        
            
        