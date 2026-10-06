dirs = input()

# Please write your code here.
"""
Trail2 시뮬레이션
dx dy technique
2026-10-06

방향 회전 해보기
"""

"""
방향 전환은 이렇게 하는 거구나
좋은거 배웠다
"""

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0 , 1]
dir = 3

for i in range(len(dirs)):
    if dirs[i] == 'L':
        dir = (dir + 3) % 4
    elif dirs[i] == 'R':
        dir = (dir + 1) % 4 
    elif dirs[i] == 'F':
        x += dx[dir]
        y += dy[dir]

print(f'{x} {y}')