# 차량별 주차 요금 계산
# 00:00 ~ 23:59 까지 누적으로 처리 -> 요금 일괄 정산
# 다음날 출차는 고려 X
# 요금 계산 시 '올림' 처리
# 차량 번호가 작은 자동차부터, 차례대로 return!
import math
# 초과 시간 올림 처리

def solution(fees, records):
    # 차량 정보 : {차량 번호 : 시간, 기록 횟수}
    car_info = {}
    # 정산 정보
    fee_list = []
    # 최대 시간 : 23:59에 나갔다고 가정
    max_time = 23 * 60 + 59
    for record in records:
        t, c, _ = record.split(" ")
        t = int(t[:2]) * 60 + int(t[3:])
        # 차량 정보 등록
        if c not in car_info:
            car_info[c] = [0, 0]
        # 시간 등록
        car_info[c][0] += ((max_time - t) * (-1) ** (car_info[c][1]))
        # 기록 횟수 증가
        car_info[c][1] += 1
    # 번호 순으로 정렬
    for _, t in sorted(car_info.items(), key = lambda x : x[0]):
        # 초과 시간
        extra_t = t[0] - fees[0] if t[0] > fees[0] else 0
        # 요금 계산 : 기본 요금 + (초과 시간) * 추가 요금
        fee = fees[1] + math.ceil((extra_t) / fees[2]) * (fees[3])
        fee_list.append(fee)
    return fee_list