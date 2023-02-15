# 길이가 1인 모든 단어를 포함 하도록 사전 초기화 -> 알파벳 입력
# 현재 입력과 일치하는 가장 긴 문자열 w 찾기 -> 한 글자씩 더해가면서 있는지 확인 -> 만약 없다면, 새로 등록해야함!
# w에 해당하는 색인 번호 출력 -> 존재하는 색인의 번호만 출력
# 없는 단어면 w + c에 해당하는 단어를 등록
from string import ascii_uppercase
 
def solution(msg):
    # 색인 번호
    idx_list = []
    # 단어 사전
    word_dict = dict(zip(ascii_uppercase, range(1, 27)))
    idx = 26
    while msg:
        # 현재 입력
        temp_msg = ""
        for i in range(len(msg)):
        	# 새로운 단어 만들기
            temp_msg += msg[i]
            # 입력이 사전에 없는 경우 새로 저장
            if temp_msg not in word_dict:
                idx += 1
                word_dict[temp_msg] = idx
                # 이전 단어의 색인 출력
                temp_msg = temp_msg[:-1]
                idx_list.append(word_dict[temp_msg])
                break
        # msg 초기화
        msg = msg[len(temp_msg):]
        # 마지막 단어가 사전에 있는 경우
        if not msg:
            idx_list.append(word_dict[temp_msg])
    return idx_list