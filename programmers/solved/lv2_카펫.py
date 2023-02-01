# 노란 박스 정보 : 가로 x 세로
# brown = ((가로 + 2) * 2 + 세로 * 2)
def solution(brown, yellow):
    answer = [0, 0]
    # yellow 박스의 가로 정보 확인
    # 가로 길이는 세로 길이 보다 크거나 같기 때문에, 제곱근 까지만 탐색
    for i in range(yellow, int(yellow ** 0.5) - 1, -1):
        # 약수인 경우
        if yellow % i == 0:
            if brown == ((i + 2) * 2 + ((yellow) // i) * 2):
                answer = [i + 2, (yellow // i) + 2]
                break
    return answer