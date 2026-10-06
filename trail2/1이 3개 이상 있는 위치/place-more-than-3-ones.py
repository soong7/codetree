n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
Trail2 시뮬레이션
dx dy technique
격자에서의 dx dy

N x N 격자에서 상하좌우 1인 칸이
3개 이상인 칸
이 몇 개인지
"""

"""
이걸 스스로 해냄
자랑스럽다
"""

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

ans = 0
for x in range(n):
    for y in range(n):
       cnt = 0
       for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt +=1
        if cnt == 3:
            ans += 1
            break

print(ans)