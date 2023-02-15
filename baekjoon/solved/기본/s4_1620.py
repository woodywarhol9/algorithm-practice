import sys

N, M = map(int, input().split())

pokemon_num = {sys.stdin.readline().rstrip() : str(i + 1) for i in range(N)}
num_pokemon = {v : k for k, v in pokemon_num.items()}

for _ in range(M):
    check = sys.stdin.readline().rstrip()
    if check in pokemon_num:
        print(pokemon_num[check])
    if check in num_pokemon:
        print(num_pokemon[check])
