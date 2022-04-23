# 몇개가 입력되는지 명시 안돼있기 때문에 사용
import sys

braket_list = ["(", ")", "[", "]"]
braket_pair = {"(" : ")", "[" : "]"}

while True:
    data = sys.stdin.readline().rstrip()
    if data == ".":
        break
    # 문자 비교
    # "("와 ")"를 비교 
    stack_braket = []
    for str in data:
        # 괄호가 아닌 경우 
        if str not in braket_list:
            continue
        # () 처리
        if str == "(" or str ==  "[":
            stack_braket.append(str)
        elif str == ")" or str == "]":
            try:
                last_braket = stack_braket.pop()
                if str != braket_pair[last_braket]:
                    print("no")
                    break                
            except:
                print("no")
                break
    else:
        if len(stack_braket) != 0:
            print("no")
        else:
            print("yes")