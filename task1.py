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
#4
#3. Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
import random

ran_num = random.randint(1,10),
user_guess = int(input("Try guess a number between 1 and 9:"))
while (user_guess!=ran_num) or (user_guess2!=ran_num):
    user_guess2 = int(input("Try again guess a number between 1 and 9:"))
      
print("well done correct guess")

#6
#Write a Python program to count the number of even and odd numbers in a series of numbers
numbersran = range(1,11) 
count_odd = 0
count_even = 0
for num in numbersran:
        if not num % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

