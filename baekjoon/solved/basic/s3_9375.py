T = int(input())

for _ in range(T):
    n = int(input())
    cloth_type = {}
    case_num = 1
    for _ in range(n):
        name, t = input().split()
        if t not in cloth_type:
            cloth_type[t] = []
        cloth_type[t].append(name)
    type_list = list(cloth_type.keys())
    # type의 옷을 입거나 벗는 경우
    for t in type_list:
        case_num *= (1+len(cloth_type[t]))
    # 모든 type의 옷을 입지 않는 경우
    case_num -= 1
    print(case_num)        
        