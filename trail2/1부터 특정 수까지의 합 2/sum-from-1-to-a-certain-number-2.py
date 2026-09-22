N = int(input())

# Please write your code here.

def sumsum(num):
    if num == 1:
        return 1
    return sumsum(num - 1) + num

print(sumsum(N))