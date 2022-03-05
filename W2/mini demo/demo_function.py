
def main():
    print('The sum of 10 and 46 is')
    show_sum(10, 46)
    
    show_interest(rate=0.01, periods=10, principal=10000.0)
    firstname, lastname = getNames()
    print (f'Name: {lastname}, {firstname}')
    
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f'The simple interest will be ${interest:,.2f}.') 

def getNames():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    
    return first_name, last_name


if __name__ == "__main__":
    main()
