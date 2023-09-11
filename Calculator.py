print("Enter the operator you want to exscute by choosing the corresponding numbers... ")
print("1.Add +")
print("2.Subtract -")
print("3.Multiply *")
print("4.Divide /")
print("5.To the Power ^")

operator = input("Enter operator Number: ")
firstnum = float(input("Enter first number: "))
secnum = float(input("Enter second number: "))
        

if operator == '1':
    print(firstnum, "+", secnum, "=", firstnum + secnum)

elif operator == '2':
    print(firstnum, "-", secnum, "=", firstnum - secnum)

elif operator == '3':
    print(firstnum, "x", secnum, "=", firstnum * secnum)

elif operator == '4':
    print(firstnum, "/", secnum, "=", firstnum / secnum)

elif operator == '5':
    print(firstnum, "**", secnum, "=", firstnum ** secnum)
     
else:
    print("Invalid Operation")