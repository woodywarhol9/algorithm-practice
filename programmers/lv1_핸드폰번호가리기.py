def solution(phone_number):
    result = "*" * (len(phone_number) - 4) + phone_number[-4:]
    return result