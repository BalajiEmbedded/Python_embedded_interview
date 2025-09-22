str1 = input("enter the string\n")


def reverse_str(str1):
    list1 = str1.split(" ")
    reversed_list = []
    for i in range(len(list1)):
        reversed_list.append(list1[i][::-1])

    return reversed_list


res = reverse_str(str1)
for i in range(len(res)):
    print(res[len(res) - 1 - i], end=" ")