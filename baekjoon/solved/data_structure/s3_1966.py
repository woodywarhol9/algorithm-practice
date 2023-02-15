from collections import deque

test_case = int(input())

for _ in range(test_case):
    # 문서 수, 순서
    n, idx = map(int, input().split())
    order_list = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        # 숫자 보관(이때 숫자를 idx와 같게 부여.)
        num_queue = deque([i for i in range(n)])
        order_queue = deque(order_list)
        max_order = max(order_queue)
        count = 0
        while True:
            if order_queue[0] == max_order:
                count += 1
                if num_queue[0] == idx:
                    print(count)
                    break
                # queue에서 순서와 숫자 제거.
                num_queue.popleft()
                order_queue.popleft()
                max_order = max(order_queue)
            else:
                # 다시 뒤로 붙임.
                num_queue.append(num_queue.popleft())
                order_queue.append(order_queue.popleft())