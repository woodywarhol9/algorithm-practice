"""
대용량 데이터 입력 : input() 대신 sys 활용
"""
import sys
input_data = sys.stdin.readline().rstrip() #입력 후 줄바꿈 기호 없애기 위해서 rstrip

print(input_data)