import sys

n = int(input())
# 순열 입력
sequence = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# 처음 실행 용
is_first = 1
# 마지막 실행된 수 : push, pop 구별
last_num = 0
# 어떤 수를 push할 지 결정
push_count = 0

for i in sequence:
    # 초기 입력 처리
    if is_first == 1:
        # 초기 입력 stack에 저장
        num_stack = [n for n in range(1, i)]
        push_pop = ["+" for _ in range(i)] + ["-"]
        # 변수 변경
        is_first = 0
        push_count = i
        last_num = i
        continue
    # 다음 수가 더 클 경우 : push 실행해야할 경우
    if last_num < i:
        # push 명령 수행
        num_stack += [n for n in range(push_count + 1, i)]
        push_pop += ["+" for _ in range(push_count + 1, i + 1)]
        push_pop.append("-")
        # 변수 변경
        push_count = i 
        last_num = i
    # 다음 수가 더 작을 경우 : pop 실행해야될 경우
    else:
        temp = num_stack.pop()
        push_pop.append("-")
        last_num = i
        # 만약 stack의 마지막 수가 i와 다를 경우
        if i != temp:
            print("NO")
            break  
else:
    print(*push_pop, sep ="\n")