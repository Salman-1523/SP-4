list1 = []

n= int(input("\nEnter list size: "))

print("Enter Number: ")

for i in range(n):
    data=int(input())
    list1.append(data)
print(f"The stack is: {list1}")

for data in list1:
    if data<0:
        print(data,end="")

list2 = [data for data in list1 if data<0]
print(f"\nThe list2 is : {list2}")

list2.pop(data<0)
print(f"\nThe pop list is : {list2}")
list2.pop(data<0)
print(f"\nThe pop list is : {list2}")
