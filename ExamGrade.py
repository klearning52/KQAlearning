level = int(input("What Level did you study 1 or 2? "))
studentGrade = int(input("What mark did you score? "))

if level == 1:
    if studentGrade > 100 or studentGrade < 1 :
        print("'Error: marks must be between 1 and 100")
    elif studentGrade >= 71:
         print(" Distinction")
    elif studentGrade >= 61:
        print(" Merit")
    elif studentGrade >= 50:
         print(" Pass")
    else:
         print(" Fail")

else:
    if studentGrade > 100 or studentGrade < 1 :
        print("'Error: marks must be between 1 and 100")
    elif studentGrade >= 66:
         print(" Distinction")
    elif studentGrade >= 51:
         print(" Merit")
    elif studentGrade >= 40:
         print(" Pass")
    else:
         print(" Fail")