def solution(numbers, hand):
    # 현재 손가락 위치
    pos_left = 9
    pos_right = 11
    
    hand = hand[0].upper()
    answer = ""
    for i in numbers:
        i -= 1
        if i == -1 : i = 10
        # 이동해야할 좌표
        x, y = divmod(i, 3)
        if y == 0:
            pos_left = i
            answer += "L"
        elif y == 2:
            pos_right = i
            answer += "R"
        else:
            x_left, y_left = divmod(pos_left, 3)
            x_right, y_right = divmod(pos_right, 3)
            # 거리 확인
            dis_left = abs(x - x_left) + abs(y - y_left)
            dis_right = abs(x - x_right) + abs(y - y_right)
            
            if dis_left > dis_right:
                answer += "R"
                pos_right = i
            elif dis_left < dis_right:
                answer += "L"
                pos_left = i
            else:
                if hand == "R":
                    pos_right = i
                else:
                    pos_left = i
                answer += hand
            
    return answer