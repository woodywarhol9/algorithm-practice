"""
라이브러리 사용해도 상관없으니 필요하면 쓰자.
"""
import math
up, down, height = map(int, input().split())
# 하루에 올라가는 거리
day_up = up - down
# 남은 거리
distance = height - up

print(math.ceil(distance / day_up) + 1)