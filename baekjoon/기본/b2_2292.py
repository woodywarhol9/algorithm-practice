"""
몇 층에 속해있는 지만 확인하면 됨! 
N층 : 6^(n)개 원소
"""

N = int(input())
sum = 1
count = 0

while True:
    if (N - sum) <= 0:
        print(count + 1)
        break
    count += 1
    sum += (count * 6)

    