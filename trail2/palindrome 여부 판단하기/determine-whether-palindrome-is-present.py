A = input()

# Please write your code here.
def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[(len(str) - 1) - i]:
            return "No"
    return "Yes"

print(isPalindrome(A))