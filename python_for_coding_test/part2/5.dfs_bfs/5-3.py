"""
재귀 함수(Recursive Function) : 자기 자신을 다시 호출하는 함수
- 실행 시 maxmimum recursion depth error 발생!
"""

def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function() # 자기 자신을 다시 호출
    
recursive_function()