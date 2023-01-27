def solution(n, lost, reserve):
    # 빌려줄 수 있는 학생 재확인
    for i in lost[:]:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    # 정렬 안된 경우 처리
    lost.sort()
    reserve.sort()
    
    cnt = n - len(lost)
    for i in lost:
        if i - 1 in reserve[:]:
            reserve.remove(i - 1)
            cnt += 1
        elif i + 1 in reserve[:]:
            reserve.remove(i + 1)
            cnt += 1
    return cnt