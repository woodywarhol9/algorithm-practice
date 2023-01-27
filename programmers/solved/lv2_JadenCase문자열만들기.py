def solution(s):
    answer = ""
    word = ""
    for char in s:
        if char == " ":
            answer += (word + " ")
            word = ""
        else:
            if not word:
                word += char.upper()
            else:
                word += char.lower()
    # 마지막 부분
    answer += word
    return answer
"""
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize()
        # i가 공백이더라도 " " 가 더해지면서 오류 발생 X
        else:
            answer += ' '+i.capitalize()
    return answer
"""