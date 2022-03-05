
BONUS_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = show_bonus(gross_pay)
    print('Salary ${:,.2f} , Bonus ${:,.2f}'.format(gross_pay,bonus))       
    
def show_bonus(gross):
    return gross * BONUS_RATE
    


if __name__ == "__main__":
    main()