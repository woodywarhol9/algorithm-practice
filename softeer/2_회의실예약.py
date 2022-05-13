import sys
# 시간 - idx 변환
hour = dict(zip(range(9, 19), range(10)))
idx2hour = dict(zip(range(10), range(9, 19)))
# 방/미팅 수
room_num, meeting_num = map(int, input().split())
# 방 이름 입력
room_name = [input() for _ in range(room_num)]

room_hour = {}
# 방 별 가능 시간 초기화
for name in room_name:
    room_hour[name] = [1 for _ in range(10)]
for _ in range(meeting_num):
    name, start, end = input().split()
    start, end = hour[int(start)], hour[int(end)]
    for idx in range(start, end):
        room_hour[name][idx] = 0
# 알파벳 순 정렬
room_hour = sorted(room_hour.items(), key = lambda x : x[0])
# 마지막 방 
last_room = room_hour[-1][0]
# 방 별로 조회
for name, hour_list in room_hour:
    print(f"Room {name}:")
    # 시작점, 끝점, 개수 초기화
    start, end = 0, 0
    count = 0
    # 출력할 시간 정보 저장
    message = []
    # 시간 정보 조회
    for idx, empty in enumerate(hour_list):
        # 시작 점
        if empty == 1 and start == 0 and idx != len(hour_list) - 1:
            start = idx2hour[idx]
        # 중간 점
        if empty == 0 and start != 0:
            end = idx2hour[idx]
            message.append(f'{start:02}-{end:02}')
            # 시작, 끝점 초기화
            start, end = 0, 0
            count += 1
        # 끝점까지 1인 경우
        if empty == 1 and start != 0 and idx == len(hour_list) - 1:
            end = idx2hour[idx]
            message.append(f'{start:02}-{end:02}')
            count += 1
    if count == 0:
        print("Not available")
    else:
        print(f"{count} available:")
        print(*message, sep = "\n")
    if name != last_room:
        print("-----")
