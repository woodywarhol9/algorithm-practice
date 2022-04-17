"""
시간 복잡도 1로 만들기 위해서 linked list로 구현
- 시간 복잡도 1인데도 시간 초과가 나와 pypy로 변경해서 통과
"""
import sys
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue():
    def __init__(self):
        self.f = None
        self.r = None
        self.num = 0
    # push 함수
    def push(self, x : int):
        temp = Node(x)
        if not self.f:
            self.f = self.r = temp
        else:
            self.r.next = temp
            self.r = temp
        self.num += 1    
    # pop 함수    
    def pop(self):
        if self.num == 0:
            print(-1)
            return
        print(self.f.data)
        temp = self.f
        self.f = temp.next
        self.num -= 1
    # size 함수
    def size(self):
        print(self.num)
    # empty 함수
    def empty(self):
        print(1 if self.num == 0 else 0)
    # front 함수
    def front(self):
        if self.num == 0:
            print(-1)
            return
        print(self.f.data)
    # back 함수
    def back(self):
        if self.num == 0:
            print(-1)
            return
        print(self.r.data)

queue = Queue()
# 명령어 미리 저장
case = {
    "pop" : lambda queue : queue.pop(),
    "size" : lambda queue : queue.size(),
    "empty" : lambda queue : queue.empty(),
    "front" : lambda queue : queue.front(),
    "back" : lambda queue : queue.back()
    }
    
n = int(input())
for _ in range(n):
    # 명령 수가 많아서 sys로 받음
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    else:
        case[command[0]](queue)