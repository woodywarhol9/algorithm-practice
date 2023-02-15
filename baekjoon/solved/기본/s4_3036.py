N = int(input())
radius_list = list(map(int, input().split()))

def get_gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r        
    return a

ring_first = radius_list[0]

for ring_temp in radius_list[1:]:
    gcd = get_gcd(ring_first, ring_temp)
    print(f'{ring_first // gcd}/{ring_temp // gcd}')