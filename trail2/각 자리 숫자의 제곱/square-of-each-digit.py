N = int(input())

# Please write your code here.

"""
Trail2
Lesson 2. 값을 반환하는 재귀함수
2026-09-22

(num % 10)을 squareSum(num % 10)이라고 적어서 에러뜸
"""

def squareSum(num):
    if num < 10:
        return num ** 2
    return squareSum(num // 10) + (num % 10) ** 2

print(squareSum(N))