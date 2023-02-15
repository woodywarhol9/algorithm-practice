from itertools import combinations

card, num = map(int, input().split())
card_list = list(map(int ,input().split()))

card_comb = list(combinations(card_list, 3))

max_sum = 0
for a, b, c in card_comb:
    sum = a + b + c
    if sum > max_sum and sum <= num:
        max_sum = sum
    
print(max_sum)