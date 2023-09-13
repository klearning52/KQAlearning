def caltax(amount, percent):
    return (amount * percent) / 100

def  getIncomeTax(x):
    total_income = x - 11850
    if total_income <= 34500:
        return caltax(total_income,20)
    elif total_income >= 34501 and total_income <= 150000:
        return caltax(total_income,40)
    else:
        return caltax(total_income,45)



income = int(input("how much do you make"))
print(getIncomeTax(income))