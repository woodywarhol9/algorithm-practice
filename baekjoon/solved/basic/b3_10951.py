"""
테스트 케이스 종료 조건이 없다면 try - except 사용해보기.
"""

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
        