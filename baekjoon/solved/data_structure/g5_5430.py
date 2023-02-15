from collections import deque

test_case = int(input())
for _ in range(test_case):
    commands = input()
    array_len = int(input())
    array = input()
    # 입력이 없고 commands에 "D"가 있을 경우
    # 밑에서 조건문 확인하며 시행하는 것보다 단순 탐색이 더 빠를 것으로 생각.
    if array_len == 0:
        if "D" in commands:
            print("error")
            continue
        else:
            print("[]")
            continue
    else:
        # bracket 제거 + "," 단위로 split, map으로 형 변환
        array = deque(map(int, array[1:-1].split(",")))
    # 명령 실행
    r_check = 0
    error_check = 0
    for cmd in commands:
        # 명령이 R인 경우
        if cmd == "R":
            if r_check == 1:
                r_check = 0
                continue
            else:
                r_check = 1
                continue
        # 명령이 D인 경우
        else:
            if len(array) == 0:
                error_check = 1
                print("error")
                break                                       
            if r_check == 1:
                array.pop()
            else:
                array.popleft()
    # 길이가 0이지만 error가 없으면 출력해야 함.
    if error_check == 0:
        if r_check == 1:
            array.reverse()      
        print("[", end="")
        print(*array, sep = ",", end = "")
        print("]")