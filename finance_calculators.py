import math
# Selection of what calculation to use
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll ehave to pay on a home loan")
calc = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
calc = calc.lower()

#Calculation for investment calculation
if calc == 'investment':
    money = int(input("Please enter the amount of money you are depositing:"))
    int_rate = int(input("Please enter the interest rate:"))/100
    years = int(input("Please enter the number of years you plan on investing:"))
    interest =  input("Simple or compound interest?")
    interest = interest.lower()
    if interest == 'simple':
        total = money * (1 + (int_rate*years))
    elif interest == 'compound':
        total = money * math.pow((1+int_rate),years)
    print(total)

#Calculation for bond calculation
if calc == 'bond':
    value = int(input("Please enter the value of the house:"))
    yearly_int_rate = int(input("Please enter the interest rate:"))/100
    monthly_int_rate = yearly_int_rate/12
    months = int(input("Please enter the number of months you plan on investing:"))
    repayment = (monthly_int_rate * value) / (1 - (1 + monthly_int_rate) ** -months)
    print(repayment)

else:
    print("Your input is incorrect. Please try again and enter either 'investment' or bond'")
