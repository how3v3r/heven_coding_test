from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
road = [list(map(int, list(input().strip()))) for _ in range(N)]


for y, ro in enumerate(road):
    print(ro)
    for x, pos in enumerate(ro):
        if pos == '1':
            start_x = x
            start_y = y


i = start_x
j = start_y

print(i, j)