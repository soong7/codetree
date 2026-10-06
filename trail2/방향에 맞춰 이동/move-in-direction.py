n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
"""
Trail2. 시뮬레이션
dx dy technique
2026-10-01 ~ 2026-10-06

입력 받은 방향, 거리
움직이셈
"""

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
nx, ny = 0, 0

for i in range(len(dir)):
    if dir[i] == 'N':
        dir[i] = 0
    elif dir[i] == 'E':
        dir[i] = 1
    elif  dir[i] == 'S':
        dir[i] = 2
    else:
        dir[i] = 3

for i in range(len(dir)):
    nx, ny = nx + dist[i] * dx[dir[i]], ny + dist[i] *dy[dir[i]]

print(f'{nx} {ny}')