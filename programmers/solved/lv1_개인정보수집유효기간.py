def cnt_day(day: str) -> int:
    # 날짜 정보를 '일' 단위로 변경하는 함수
    day = day.split(".")
    day = int(day[0]) * 12 * 28 + int(day[1]) * 28 + int(day[2])
    return day

# 시간은 : 0X 단위로 처리
def solution(today, terms, privacies):
    answer = []
    # 비교하기 쉽게 '일' 단위로 변경
    today = cnt_day(today)
    # key : term, value : 기간
    terms = [term.split(" ") for term in terms]
    terms = dict(zip(list(zip(*terms))[0], list(zip(*terms))[1]))
    for idx, privacy in enumerate(privacies):
        # 날짜, 약관 분리
        day, term = privacy.split(" ")
        day = cnt_day(day)
        day += (int(terms[term]) * 28)
        # 제거할 날짜 정보
        if today >= day:
            answer.append(idx + 1)
    return answer