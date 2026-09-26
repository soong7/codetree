N = int(input())

# Please write your code here.

"""
Trail2
Lesson 2. 값을 반환하는 재귀함수

Factorial
"""

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

print(factorial(N))