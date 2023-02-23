"""
처음으로 시간 초과가 발생한 문제. for문을 사용할 때 주의하자!
"""
word = input().upper()
char = list(set(word))

cnt_list = []
for c in char:
    cnt = word.count(c)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")

else:
    max_index = cnt_list.index(max(cnt_list))
    print(char[max_index])
    

    

    
