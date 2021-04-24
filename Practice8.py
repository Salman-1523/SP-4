# Summation of Series Number using While Loop

print("\nSummation of Series Number")
print("------------------------------")
#############################################
print("\nFactorial Series")

x = int(input("Enter x: "))

fact = 1
i = 1
while i<=x:
    fact=fact*i
    i=i+1
print(f"The factorial of {x} is {fact}.")
print("\n!!!Programme End!!!")

###########################################
print("\n# 1+2+3+4+...........+n=?")

n = int(input("Enter n:"))

sum=0
i=1
while i<=n:
    sum = sum + i
    i = i + 1
print(f"The sum is {sum}.")
print("\n!!Programme End!!")

################################################
print("\n# 2+4+6+8+...........+n=?")

n = int(input("Enter n: "))

sum=0
i=2
while i<=n:
    sum = sum+i
    i=i+2
print(f"The sum is {sum}.")
print("\n!!!Programme End!!!")

################################################
print("\n# 4+9+14+19+.................+n=?")

n = int(input("Enter n: "))

sum=0
i=4
while i<=n:
    sum=sum+i
    i=i+5
print(f"The sum is {sum}.")
print("\n!!!Programme End!!!")

#################################################
print("\n# 1+2+4+8+.................+n=?")

n = int(input("Enter n: "))

sum=0
i=1
while i<=n:
    sum=sum+i
    i=i*2
print(f"The sum is {sum}.")
print("\n!!!Programme End!!!")

##################################################
print("\n# 1 + 2*2 + 3*3 + 4*4 +………………+ n*2 = ?")

n = int(input("Enter n: "))

sum = 0
i = 1
while i<=n:
    sum= sum+(i*i)
    i=i+1
print(f"The sum is {sum}.")
print("\n!!!Programme End!!!")

#####################################################
print("\n# 1 + 2*3 + 4*3 + 8*3 +………………+ n*3 = ?")

n = int(input("Enter n: "))

sum = 0
i = 1
while i<=n:
    sum= sum+(i*i*i)
    i=i*2
print(f"The sum is {sum}.")
print("\n!!!Programme End!!!")

######################################################
print("\n# 2x4x6x8x...............xn=?")

n = int(input("Enter n: "))

mul=1
i=2
while i<=n:
    mul=mul*i
    i=i+2
print(f"The mul is {mul}.")
print("\n!!!Programme End!!!")

#########################################################
print("\n# 2x4x8x................xn=?")

n = int(input("Enter n: "))

mul=1
i=2
while i<=n:
    mul=mul*i
    i=i*2
print(f"The mul is {mul}.")
print("\n!!!Programme End!!!")

#############################################################
print("\n# 1 * 2*3 * 4*3 * 8*3 *………………* n*3 = ?")

n = int(input("Enter n: "))

mul = 1
i = 1
while i<=n:
    mul=mul*(i*i*i)
    i=i*2
print(f"The mul is {mul}.")
print("\n!!!Programme End!!!")

#############################################################
print("\n# 3*3 * 6*3 * 12*3 *………………* n*3 = ?")

n = int(input("Enter n: "))

mul = 1
i = 3
while i<=n:
    mul=mul*(i*i*i)
    i=i*2
print(f"The mul is {mul}.")
print("\n!!!Programme End!!!")

#############################################################
print("\n# 3*3 * 6*3 * 9*3 *………………* n*3 = ?")

n = int(input("Enter n: "))

mul = 1
i = 3
while i<=n:
    mul=mul*(i*i*i)
    i=i+3
print(f"The mul is {mul}.")
print("\n!!!Programme End!!!")