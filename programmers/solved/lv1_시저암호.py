def solution(s, n):
    sol = ""
    for char in s:
        if char == " ":
            sol += char
            continue
        else:
            ascii = ord(char)
            char_new = n + ascii
            # 대문자 처리
            if 65 <= ascii <= 90:
                if char_new > 90:
                    char_new -= 26
            # 소문자 처리
            elif 97 <= ascii <= 122:
                if char_new > 122:
                    char_new -= 26
            sol += chr(char_new)
                
    return sol

"""
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.
"""