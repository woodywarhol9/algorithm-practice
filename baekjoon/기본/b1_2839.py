sugar = int(input())
q_5, r_5 = divmod(sugar, 5)

#5로 바로 나눠지는 경우
if r_5 == 0:
    print(f'{q_5}')

else:
    # 5로 나눈 나머지가 3인 경우
    if r_5 % 3 == 0:
        print(f'{q_5 + r_5 // 3}')
    # 5 개수를 최대로 하는 경우의 수 확인
    else:
        for i in range(q_5 - 1,-1, -1):
            sugar_temp = sugar - (i * 5)
            q, r = divmod(sugar_temp, 3) 
            if r == 0:
                print(f'{i + q}')
                break
        
        else:
            # 3으로 나눠지는지 확인
            q_3, r_3 = divmod(sugar, 3)
            if r_3 == 0:
                print(f'{q_3}')
            else:
                print(-1)
                
            

