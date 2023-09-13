print("Enter the operator you want to exscute by choosing the corresponding numbers... ")
print("Find the length of A given B and C")
print("Find the length of B given A and C")
print("Find the length of A given C and B")

operator = input("Enter operator Number: ")
lengthA = float(input("Enter length of A: "))
lengthB = float(input("Enter length of B: : "))

if operator == '1':
    print(lengthA, "**2",+ , lengthB, "**2")

elif operator == '2':
    print(firstnum, "-", 
          
          secnum, "=", firstnum - secnum)

elif operator == '3':
    print(firstnum, "x", secnum, "=", firstnum * secnum)
else:
    print("Invalid Operation")