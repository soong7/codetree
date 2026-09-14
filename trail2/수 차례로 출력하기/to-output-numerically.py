n = int(input())

# Please write your code here.

def printnums1(n):
    if n == 0:
        return
    printnums1(n - 1)
    print(n, end = ' ')

def printnums2(n):
    if n == 0:
        return
    print(n, end = ' ')
    printnums2(n - 1)

printnums1(n)
print()
printnums2(n)