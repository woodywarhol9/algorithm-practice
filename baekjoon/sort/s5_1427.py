"""
문자열로 받고 정렬하기.
"""
n = input()
print(*sorted(n, reverse = True), sep = '')