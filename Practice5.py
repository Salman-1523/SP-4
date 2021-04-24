#Result

print("!!!!!!!!!! << Markshit >> !!!!!!!!!!")
print("-----------------------------------------------")

mark = float (input("Enter your maek: "))

if mark>=80 and mark<=100:
    print(f"{mark} = A+")
    print("!!Congratulation!!")
elif mark>=70 and mark<=79:
    print (f"{mark} = A")
    print("!!Congratulation!!")
elif mark>=60 and mark<=69:
    print (f"{mark} = A-")
    print("!!Congratulation!!")
elif mark>=50 and mark<=59:
    print (f"{mark} = B")
    print("!!Congratulation!!")
elif mark>=40 and mark<=49:
    print (f"{mark} = C")
    print("!!Congratulation!!")
elif mark>=33 and mark<=39:
    print (f"{mark} = D")
    print("!!Congratulation!!")
else:
    print(f"{mark} = Fail")
    print("Bring your parents.")

print("\nProgramme Done!")

#Even/Odd

print("\n!!!!!!!!!! << Even/Odd >> !!!!!!!!!!")
print("-----------------------------------------------")

num = int(input("Enter a Number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

print("\nProgramme Done!\n")

#Even/Odd/Non-Negative

print("\n!!!!!!!!!! << Even/Odd/Non-Negative >> !!!!!!!!!!")
print("----------------------------------------------------")

num = int(input("Enter a Number: "))

if num  == 0:
    print(f"{num} is Non-Negative.")
elif num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.45")

print("\nProgramme Done!\n")

# largest number between 3 number

print("\n!!!!!!!!!! << largest number >> !!!!!!!!!!")
print("-----------------------------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is Largest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is Largest")
else:
    print(f"{num3} is Largest")

print("\nProgramme End!\n")

# lowest number between 3 number

print("\n!!!!!!!!!! << lowest number >> !!!!!!!!!!")
print("-----------------------------------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print(f"{num1} is Largest")
elif num2 <num1 and num2 < num3:
    print(f"{num2} is Largest")
else:
    print(f"{num3} is Lowest")

print("\nProgramme End!\n")

#Vowel/Consonent

print("\n!!!!!!!!!! << largest number >> !!!!!!!!!!")
print("-----------------------------------------------")

ch = str(input("Enter a Alphabate: "))

if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U" :
    print(f"{ch} is Vowel.")
else:
    print(f"{ch} is Consonant.")

print("\nProgramme End!")

