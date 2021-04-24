mark1 = float (input("Enter your first scores: "))

if (mark1 >= 1 and mark1 <= 10):
    mark2 = float(input("Enter your second scores: "))
    if (mark2 >= 1 and mark2 <= 10):
        avg = (mark1+mark2)/2
        print(f"Avarage is {avg}.")
    else:
        print(f"{mark2} is not Valid.")

else:
    print(f"{mark1} is Not Valid.")