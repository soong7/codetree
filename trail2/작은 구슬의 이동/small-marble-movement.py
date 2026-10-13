n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

"""
2026-10-13
Trail 2. dx dy technique

격자 안에서
벽 박으면 반대로 가는 구슬
도착점 위치 구하기
"""

"""
딕셔너리 사용하는 아이디어 배웠다
범위 확인 할 때 0 포함해서 에러 뜸
"""

# 변수 선언
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}
dir = mapper[d]

# 범위 확인 함수
def is_valid(x, y, n):
    return x >= 1 and x <= n and y >= 1 and y <= n
    
# 움직이기
nx, ny = r, c
x, y = r, c
for i in range(t):
    nx, ny = x + dx[dir], y + dy[dir]
    if is_valid(nx, ny, n):
        x, y = nx, ny
    else:
        dir = 3 - dir

# 출력
print(f'{x} {y}') 