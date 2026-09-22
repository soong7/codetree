n = int(input())

# Please write your code here.
def star(num):
    if num == 0:
        return
    print('* ' * num)    
    star(num - 1)
    print('* ' * num)
    

star(n)