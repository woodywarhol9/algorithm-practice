# 최대 14번 반복 -> 완전 탐색 시 최악의 경우 대략 (100*100)**14의 연산 필요 -> 시간 초과
# 유클리드 호제법 활용
def solution(arr):
    # 유클리드 호제법 사용 위해 정렬
    arr.sort()
    for i in range(1, len(arr)):
        #a, b의 최대 공약수는 b, r의 최대 공약수와 같음
        a, b = arr[i], arr[i - 1]
        # lcm * gcd = a * b 성질 활용
        mul = a * b
        while b != 0:
            r = a % b
            a = b
            b = r
        # 각 성분에 lcm 저장
        arr[i] = mul // a
    return arr[-1]