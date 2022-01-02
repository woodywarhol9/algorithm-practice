"""
문자열 재정렬 : 알파벳과 숫자를 나눈 뒤 알파벳을 오름차순 정렬하여 만든 문자열과 숫자의 합으로 구성된 문자열을 서로 연결한다.
"""
S = input()

char = sorted([i for i in S if i.isalpha()])
char = "".join(char)
digit = sum([int(i) for i in S if i.isdigit()])
digit = str(digit)

print(char+digit)