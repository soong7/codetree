N = int(input())

# Please write your code here.
def happydog(num):
    if num == 0:
        return
    print(num, end=' ')
    happydog(num-1)
    print(num, end=' ')

happydog(N)