list1 = []
list2 = []

n1 = 5
n2 = 5
print("Enter Number: ")
for i in range(n1):
    data=int(input())
    list1.append(data)
for j in range(n2):
    data=int(input())
    list2.append(data)
print(list1)
print(list2)

zipped_list3=zip(list1,list2)
sum = [list1 + list2 for (list1,list2) in zipped_list3]
print(sum)
print(max(sum))