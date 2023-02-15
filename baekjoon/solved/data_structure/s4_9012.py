test_case = int(input())
for _ in range(test_case):
    data = input()
    left_num = 0
    right_num = 0
    for i in data:
        if i == "(":
            left_num += 1
        elif i == ")":
            right_num += 1
        if right_num > left_num:
            print("NO")
            break
    else:
        if left_num != right_num:
            print("NO")
        else:
            print("YES")