# 정답 : (먼저 탈락하는 사람의 번호, 몇 번째 차례에 탈락)
def solution(n, words):
    answer = [0, 0]
    # 중복 단어 체크
    word_set = set()
    last_word = ""
    # 끝말잇기 시작
    for idx, word in enumerate(words):
        # 초기 문자 없는 경우
        if not last_word:
            last_word = word
            word_set.add(last_word)
            continue
        # 끝말잇기 실패 처리
        if word in word_set or word[0] != last_word[-1]:
            answer = [idx % n + 1, idx // n + 1]
            break
        # 정상적으로 진행
        else:
            last_word = word
            word_set.add(last_word)
    return answer