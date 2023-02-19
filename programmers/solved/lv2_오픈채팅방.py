# 입장 : 닉네임이 들어옴 -> 퇴장 : 닉네임님이 나감
# 닉네임 변경 방법 : 채팅방 나간 후, 새로운 닉네임으로 다시 들어감 / 채팅방에서 닉네임 변경
# 변경 -> 기존 출력 메시지 닉넴도 변경

# 유저 구분 -> uid 활용!
# uid 변경한 경우, 기존 메시지까지 변경
# uid : 마지막 이름으로
def solution(record):
    msg_list = []
    last_name = {}
    # uid에 마지막 이름 정보 할당하기
    for r in record:
        info = r.split(" ")
        # 이름 설정/변경이 있는 경우
        if len(info) == 3:
            last_name[info[1]] = info[2]
    for r in record:
        info = r.split(" ")
        if info[0] == "Enter":
            msg_list.append(f"{last_name[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            msg_list.append(f"{last_name[info[1]]}님이 나갔습니다.") 
    
    return msg_list