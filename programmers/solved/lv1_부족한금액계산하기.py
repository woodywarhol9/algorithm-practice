def solution(price, money, count):
    total_price = count * (count + 1) * price // 2
    result = money - total_price
    
    return abs(result) if result <= 0 else 0