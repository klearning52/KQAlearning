#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
#1
listnum=[]
for num in range(1500, 2700):
    if (num%5==0) and (num%7==0):
        listnum.append(str(num))
        print (','.join(listnum))


#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#2
con = input("do you want to convert celsius into fahrenheit enter C OR fahrenheit into celsius enter F")
tmp = float(input('typer the temperature :'))
if con == "C" or "c":
    fah = tmp * 9/5 + 32
    print(f'the temperature in fahrenheit is :{fah}')
elif con == "F" or "f":
     cel = (tmp - 32) * 5/9
     print(f'the temperature in celsius is :{cel}')
else:
    print("Error: incorrect input")
