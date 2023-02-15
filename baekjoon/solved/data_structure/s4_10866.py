"""
Doubly linked list로 dequeue 구현.
"""
import sys

class Node():
    def __init__(self, data):
        # doubly linked list로 구현. 
        self.data = data
        self.next = None
        self.prev = None
        
class Dequeue():
    def __init__(self):
        self.f = None
        self.r = None
        self.num = 0
        
    def push_front(self, x : int):
        temp = Node(x)
        if self.num == 0:
            self.f = self.r = temp
        else:
            # self.f.prev는 계속 None으로 남음.
            temp.next = self.f
            self.f.prev = temp
            self.f = temp
        self.num += 1   
           
    def push_back(self, x : int):
        temp = Node(x)
        if self.num == 0:
            self.f = self.r = temp
        else:
            # self.r.next는 계속 None으로 남음.
            temp.prev = self.r
            self.r.next = temp
            self.r = temp
        self.num += 1    
               
    def pop_front(self):
        if self.num == 0:
            print(-1)
            return
        print(self.f.data)
        temp = self.f
        self.f = temp.next
        self.num -= 1
    
    def pop_back(self):
        if self.num == 0:
            print(-1)
            return
        print(self.r.data)
        temp = self.r
        self.r = temp.prev
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
        
dequeue = Dequeue()
# 명령어 미리 저장
case = {
    "pop_front" : lambda  dequeue : dequeue.pop_front(),
    "pop_back" : lambda dequeue : dequeue.pop_back(),
    "size" : lambda dequeue : dequeue.size(),
    "empty" : lambda dequeue : dequeue.empty(),
    "front" : lambda dequeue : dequeue.front(),
    "back" : lambda dequeue : dequeue.back(),
    }
    
n = int(input())
for _ in range(n):
    # 명령 수가 많아서 sys로 받음
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push_front":
        dequeue.push_front(int(command[1]))
    elif command[0] == "push_back":
        dequeue.push_back(int(command[1]))
    else:
        case[command[0]](dequeue)
            