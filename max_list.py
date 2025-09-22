list1=list(map(int,input("enter the list:").split(",")))
sums_list=[]
for i in range(0,len(list1)+1):
    for j in range(i+1,len(list1)+1):
        sums_list.append(sum(list1[i:j]))
        print(list1[i:j])
print(max(sums_list))
print(min(sums_list))
