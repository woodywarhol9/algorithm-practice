def solution(A,B):
    # 둘 중 어느 것을 뒤집어도 동일한 결과
    A.sort()
    B.sort(reverse = True)
    return sum([A[i] * B[i] for i in range(len(A))])