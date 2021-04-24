# While Loop

#Ascending Order Number print
print("Ascending Order Number print")
print("-----------------------------")

n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i)
    i=i+1
print("\n!!Programme End!!")

#Descending Order Number print
print("\nDescending Order Number print")
print("------------------------------")

n = int(input("Enter n: "))

i = n
while i >= 1:
    print(i)
    i=i-1
print("\n!!Programme End!!")


#Even Number

print("\nEven Number print")
print("------------------------------")

n = int(input("Enter n: "))

i = 2
while i <= n:
    print(i)
    i=i+2
print("\n!!Programme End!!")

#Odd Number

print("\nOdd Number print")
print("------------------------------")

n = int(input("Enter n: "))

i = 1
while i <= n:
    print(i)
    i=i+2
print("\n!!Programme End!!")

# Summation of Series Number

print("\nSummation of Series Number")
print("------------------------------")
print("\n# 1+2+3+4+...........+n=?")

n = int(input("Enter n:"))

sum=0
i=1
while i<=n:
    sum = sum + i
    i = i + 1
print(f"The sum is {sum}.")
print("\n!!Programme End!!")