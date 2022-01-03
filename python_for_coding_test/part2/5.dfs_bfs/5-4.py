"""
재귀 함수 : 종료 조건을 반드시 명시해줘야 한다.
+ 재귀 함수는 내부적으로 스택 자료구조와 동일하기 때문에 스택 자료구조를 활용해야 하면 재귀 함수를 활용하자!
"""
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursive_function(1)