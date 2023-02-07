# LRU : 최근에 사용되지 않은 캐시부터 교체
# 사용 순 -> 입력 순으로 정렬 필요
from collections import deque

def solution(cacheSize, cities):
    # 실행 시간
    answer = 0
    cache = deque()
    for city in cities:
        # 대소문자 구분 X
        city = city.lower()
        # 캐시에 city 정보가 있다면
        # 다시 맨 뒤로 보냄
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            answer += 5
        # 새로운 도시 캐싱
        if cacheSize != 0:
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
    return answer