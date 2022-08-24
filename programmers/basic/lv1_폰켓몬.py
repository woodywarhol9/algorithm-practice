from collections import Counter

def solution(nums):
    num_cnt = Counter(nums)
    return min(len(num_cnt), len(nums) // 2)