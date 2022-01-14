"""
금광 : 
"""

T = int(input())
n_list = []
m_list = []
map_list = []

for _ in range(T):
    n, m = map(int, input().split())
    map_info = list(map(int, input().split()))
    
    n_list.append(n)
    m_list.append(m)
    map_list.append(map_info)
    
    
    