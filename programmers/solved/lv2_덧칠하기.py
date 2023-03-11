# N 개의 구역 (1 ~ N 라벨)
# M 미터 -> 구역 초과 X
# 반복해도 되지만, 최소화해야 함
# 끝에서 부터 확인하면 될 듯 -> 윈도우가 범위 안 넘어가면 색칠
# 순서 유지돼야 함 -> 윈도우 내 최소 값 보다 마지막 성분이 큰 경우 pop()
def solution(n, m, section):
    cnt = 0
    # 모든 영역을 다 칠할 때 까지 반복
    while section:
        # 윈도우 설정
        end = section[-1] - 1
        start = end - m + 1
        # 범위 초과 경우
        if start < 0:
            start, end = 0, m - 1
        cnt += 1
        while start <= (section[-1] - 1):
            section.pop()
            # 다 제거한 경우
            if not section:
                break
    return cnt