def solution(s):
    idx = 0
    s_new = ""
    for char in s:
        if char == " ":
            idx = 0
            s_new += char
            continue
        else:
            if idx % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            idx += 1
            s_new += char
            
    return s_new
        