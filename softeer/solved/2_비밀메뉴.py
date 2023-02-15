import sys
# 레시피, 유저 입력, 버튼 수
secret_num, seq_num, button_num = map(int, input().split())
# 레시피 / 유저 정보 입력
secret = list(map(int, input().split()))
seq = list(map(int, input().split()))
# 후보 
seq_list = [] 

# 사용자 입력이 더 짧을 경우
if secret_num > seq_num:
    print("normal")
else:
    for idx, i in enumerate(seq):
        # seq 단위로 저장
        if i == secret[0]:
            seq_list.append(seq[idx:idx + secret_num])

    for lst in seq_list:
        if lst == secret:
            print("secret")
            break
    else:
        print("normal")