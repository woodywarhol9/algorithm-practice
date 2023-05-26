S = input()
for i in range(len(S)):
    if S[i:] == S[i:][::-1]:
        palindrome = S + S[:i][::-1]
        print(len(palindrome))
        break