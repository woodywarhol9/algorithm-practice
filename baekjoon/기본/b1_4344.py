C = int(input())

for _ in range(C):
    test_case = list(map(int, input().split()))
    n, score_list = test_case[0], test_case[1:]
    mean = sum(score_list) / n
    score_list = [i for i in score_list if i > mean]
    print(f'{len(score_list)*100 / n:.3f}%')
    
    