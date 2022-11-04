from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck_weights = deque(truck_weights)
    # 다리에 트럭이 진입한 시간
    time_list = deque()
    # 현재 다리 위 트럭 무게
    weight_now = deque()
    # 총 시간
    answer = 0
    # 모든 트럭 진입 후 종료
    while truck_weights:
        # 진입할 트럭
        temp_weight = truck_weights[0]
        # 무게 + 트럭 개수 만족
        if (sum(weight_now) + temp_weight <= weight) and len(time_list) < bridge_length:
            # 다리 위 무게
            weight_now.append(truck_weights.popleft())
            time_list.append(answer)
        # 트럭 진입 : 시간 경과
        answer += 1
        # 통과 조건
        if (answer - time_list[0]) == bridge_length:
            weight_now.popleft()
            time_list.popleft()
    # 마지막 진입한 트럭이 나올 때까지의 시간
    answer += (bridge_length)
    
    return answer