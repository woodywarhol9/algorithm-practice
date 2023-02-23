# 길이 5 이하의 단어
# 중복 순열 만들어도 시간 초과 X
from itertools import product
 
def solution(word):
    word_dic = set()
    for p in product(["", "A", "E", "I", "O", "U"], repeat = 5):
        word_dic.add("".join(p))
    word_dic = sorted(word_dic)
    for idx, w in enumerate(word_dic):
        if w == word:
            return idx