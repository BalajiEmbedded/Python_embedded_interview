def ispalindrome(str1):
    for i in range(len(str1)):
        if(str1[i]!=str1[len(str1)-1-i]):
            return False
    return True

res=ispalindrome("madam")

if res:
    print("it is palindrome")
else:
    print("it is not a palindrome")

