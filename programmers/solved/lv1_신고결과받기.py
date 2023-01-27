def solution(id_list, report, k):
    # 사용자를 신고한 유저
    user_report = {}
    report = list(set(report))
    # 신고 처리
    for i in report:
        a, b = i.split(" ")
        # 신고 처리
        if b not in user_report:
            user_report[b] = set()
        user_report[b].add(a)
    # 메일 개수
    mail_cnt = dict(zip(id_list, [0] * len(id_list)))
    for uid, u_list in user_report.items():
        if len(u_list) >= k:
            # 해당 유저를 신고한 유저 모음
            for u in u_list:
                mail_cnt[u] += 1
    answer = []
    for u in id_list:
        answer.append(mail_cnt[u])
        
    return answer