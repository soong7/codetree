N = int(input())

# Please write your code here.
"""
Trail2
Lesson 2. 값을 반환하는 재귀함수

홀수 짝수에 따른 출력값
N이 홀수면 1부터 N까지의 홀수의 합
N이 짝수면 2부터 N까지의 짝수의 합
"""

def horse(n):
    if n == 1 or n == 2:
        return n
    return horse(n - 2) + n

print(horse(N))