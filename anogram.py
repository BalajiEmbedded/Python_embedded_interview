def isanogram(str1,str2):
    if(len(str1) == len(str2)):

        for i in range(len(str1)):
            if str1[i] in str2:
                if(i==len(str1)-1):
                    return True
            else:
                return False
    else:
        return False

res=isanogram("eat","tet")

if res:
    print("it is anogram")
else:
    print("it is not anogram")