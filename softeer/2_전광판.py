import sys
# 맨 위 idx를 0, 왼쪽을 1, 오른쪽을 2 아래를 3 ... 방식으로 숫자를 만들 경우 필요한 전구 미리 정의
num2lamp = {
    "0" : set([0, 1, 2, 4, 5, 6]),
    "1" : set([2, 5]),
    "2" : set([0, 2, 3, 4, 6]),
    "3" : set([0, 2, 3, 5, 6]),
    "4" : set([1, 2, 3, 5]),
    "5" : set([0, 1, 3, 5, 6]),
    "6" : set([0, 1, 3, 4, 5, 6]),
    "7" : set([0, 1, 2, 5]),
    "8" : set([0, 1, 2, 3, 4, 5, 6]),
    "9" : set([0, 1, 2, 3, 5, 6]),
    " " : set()
        }
# test case 수
test_case = int(input())
for _ in range(test_case):
    num_a, num_b = input().split()
    # zero padding
    num_a = num_a.rjust(5, " ")
    num_b = num_b.rjust(5, " ")
    count = 0
    for a, b in zip(num_a, num_b):
        # 같을 경우 개수 안 세도 됨
        if a == b:
            continue
        else:
            # a에만 있으면 꺼야함
            off = len(num2lamp[a] - num2lamp[b])
            # b에만 있으면 켜야함
            on = len(num2lamp[b] - num2lamp[a])
            count += int(on + off)
    # 결과 출력                
    print(count)