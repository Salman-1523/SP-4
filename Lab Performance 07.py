list1 = []

choice = input("\nHow did you want to calculate your expenses (Day/Hour): ")

if choice == "Day":
    n = int(input("\nHow many Expenses: "))
    for n in range(n):
        Expenses = int(input(f"\nEnter Expenses: "))
        list1.append(Expenses)


else:
    if choice == "Hour":
        n = int(input(f"\nHow many Expenses: "))
        for n in range(n):
            Expenses = int(input("Enter Expenses: "))
            list1.append(Expenses)

    else:
        print("\nPlease give your expenses in Day/Hour")

print(f"\nTotal Expenses is {choice}=", sum(list1))