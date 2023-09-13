
def cal(amount, percent):
    return (amount * percent) / 100

def  getIncomeTax(income1):
    total_income = income - 11,850
    if total_income <= 34500:
        return cal(total_income,20)
    elif total_income >= 34501 and total_income <= 150000:
        return cal(total_income,40)
    else:
        return cal(total_income,45)
   


    
income =input("how much cheese do you earn? £")
print(getIncomeTax(income))


 