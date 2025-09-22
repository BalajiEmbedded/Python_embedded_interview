list1=list(map(int,input("enter the list elements:").split(",")))

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]>list1[j]):
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
print(list1)