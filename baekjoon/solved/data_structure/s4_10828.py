import sys

class Node():
    def __init__(self, x : int):
        self.data = x
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.num = 0
        
    def push(self, x : int):
        temp = Node(x)
        if self.num == 0:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
        self.num += 1
    
    def pop(self):
        if self.num == 0:
            print(-1)
            return
        print(self.head.data)
        temp = self.head
        self.head = temp.next
        self.num -= 1
    
    def size(self):
        print(self.num)
    
    def empty(self):
        print(1 if self.num == 0 else 0)
        
    def top(self):
        print(self.head.data if self.num != 0 else -1)

n = int(input())
stack = Stack()
#case문 역할
case = {
    "pop" : lambda stack : stack.pop(),
    "size" : lambda stack : stack.size(),
    "empty" : lambda stack : stack.empty(),
    "top" : lambda stack : stack.top()
}

for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "push":
        stack.push(cmd[1])
    else:
        case[cmd[0]](stack)