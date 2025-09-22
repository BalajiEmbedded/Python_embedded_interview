
list1=list(map(int,input("enter the list elements:").split(",")))

largest=list1[0]

for i in list1:
    if i>largest:
        largest=i
print(largest)
