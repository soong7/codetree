n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
"""
이렇게 하면 안됨... 나의 실수
for num in arr:
    if num % 2 == 0:
        num //= 2
"""

for i in range(n):
    if arr[i] % 2 == 0:
        arr[i] //= 2

print(*arr)