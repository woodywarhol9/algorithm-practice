def solution(a, b):
    mon_31 = [1, 3, 5, 7, 8, 10, 12]
    mon_30 = [4, 6, 9, 11]
    mon_29 = [2]
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    day = 0
    for i in range(1, a):
        if i in mon_31:
            day += 31
        elif i in mon_30:
            day += 30
        elif i in mon_29:
            day += 29
    
    day += (b - 1)
    return day_list[day % 7]