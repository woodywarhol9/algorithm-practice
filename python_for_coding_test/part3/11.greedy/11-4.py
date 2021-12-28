"""
만들 수 없는 금액 : 오름차순으로 정렬 후 target 값과 비교!
"""
N = int(input())
coin = sorted(list(map(int, input().split())))

target = 1
for i in coin:
    if target < i:
        break
    target += i
print(target)