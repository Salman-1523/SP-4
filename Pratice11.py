########################################################
print("Write a programme that will take n amount of input from the users and then put them into two different list.\nAfter that it will add the first element of list1 with the first element of list2.\nThis process will repeat untill all the elements are finished.\nAfter that put the result in another list.\nThen find out the maximum and minimum from that list.")

list1 = []
list2 = []
list3 = []

n = int(input("\nEnter Size of List: "))

print("Enter Number: ")
i=0
for i in range(n):
    data=int(input())
    list1.append(data)
j=0
for j in range(n):
    data=int(input())
    list2.append(data)
i=0
j=0
k=0
for k in range(n):
    sum = list1[i] + list2[j]
    i=i+1
    j=j+1
    list3.append(sum)

print(f"List1= {list1}")
print(f"List2= {list2}")
print(f"List3= {list3}")
print(f"The maximum number is {max(list3)}.")
print(f"The minimum number is {min(list3)}.")
print("\n!!!programme End!!!")