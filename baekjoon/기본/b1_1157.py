from collections import Counter

word = input()
char_count = Counter(word.lower())
print(max(char_count))
