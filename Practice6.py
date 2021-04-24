#Inner if

# largest number between 3 number

print("\n!!!!!!!!!! << largest number >> !!!!!!!!!!")
print("-----------------------------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Largest.")
    else:
        print(f"{num3} is Largest.")

if num2 > num1:
    if num2 > num3:
        print(f"{num2} is Largest.")
    else:
        print(f"{num3} is Largest.")

print("\nProgramme End!")

# lowest number between 3 number

print("\n!!!!!!!!!! << lowest number >> !!!!!!!!!!")
print("-----------------------------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 < num2:
    if num1 < num3:
        print(f"{num1} is Lowest.")
    else:
        print(f"{num3} is Lowest.")

else:
    if num2 < num3:
        print(f"{num2} is Lowest.")
    else:
        print(f"{num3} is Lowest.")

print("\nProgramme End!")

#Alphabets/Vowel/Consonant/Number/Symbol

print("Alphabets/Vowel/Consonant/Number/Symbol")
print("------------------------------")

ch = input("Enter a Character: ")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(f"{ch} is Alphabets")
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print(f"{ch} is Vowel.")
    else :
        print(f"{ch} is Consonant.")

else :
    print(f"{ch} is Number or Symbol.")
    if (ch >= '0' and ch <= '9'):
        print(f"{ch} is number.")
    else:
        print(f"{ch} is Symbol.")

print("\n!!!Programme End!!!")