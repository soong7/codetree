A = input()

# Please write your code here.
def checking(str):
    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            return 'Yes'
    return 'No'

print(checking(A))