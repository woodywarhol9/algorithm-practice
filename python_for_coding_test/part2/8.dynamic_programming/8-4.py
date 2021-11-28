"""
피보나치 : 반복문으로 해결하기. (Bottom-up 방식)
"""

#계산된 결과 저장
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수(fibonacci Function) 반복문으로 구현(bottom-up)
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]