n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
"""
Trail2 dx dy technique
2026-10-14

빙빙 돌며 수로 직사각형 채우기
"""

"""
arr[0][0] = 1이어야 하는데
arr[0][0] = 0으로 적어서
while 무한루프 돌아버려서 시간 초과 뜸
발견하느라 한참 걸림
"""

# 변수 선언
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir = 0

arr[0][0] = 1
t = 2

# 범위 검사
def in_range(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m

# 달팽이 모양으로 수 채우기
while(t <= n * m):
    nx, ny = x + dx[dir], y + dy[dir]
    if in_range(nx, ny, n, m) and arr[nx][ny] == 0:
        x, y = nx, ny
        arr[x][y] = t
        t += 1
    else:
        dir = (dir + 1) % 4

# 출력하기
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()