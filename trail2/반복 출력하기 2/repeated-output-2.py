n = int(input())

# Please write your code here.

def helloworld(count):
    if count == 0:
        return
    helloworld(count - 1)
    print('HelloWorld')


helloworld(n)