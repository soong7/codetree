N = int(input())

# Please write your code here.

"""
Trail2
Lesson 2. 값을 반환하는 재귀함수
2026-09-26

재귀함수를 이용한 피보나치 수
"""

def fun(n):
    if n == 1 or n == 2:
        return 1
    return fun(n - 1) + fun(n - 2)

print(fun(N))