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
    

    

    
