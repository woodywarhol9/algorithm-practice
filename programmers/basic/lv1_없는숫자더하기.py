def solution(numbers):
    num_list = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    return sum(num_list - set(numbers))