N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
max_i = score_list.index(max_score)

for i in range(N):
    score_list[i] = (score_list[i] / max_score) * 100 
       
print(sum(score_list) / N)