N = int(input())

# Please write your code here.

"""
Trail2
Lesson 2. 값을 반환하는 재귀함수
2026-09-25

정수 N에 대하여
짝수 -> 2로 나눈 몫
홀수 -> 3으로 나눈 몫
1이 될 때 까지 진행한 작업 횟수 구하기
"""

def toOne(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return toOne(n // 2) + 1
    else:
        return toOne(n // 3) + 1

print(toOne(N))