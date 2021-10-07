name = input("Please enter your name: ")

money_under_the_mattress = float(input(name + ", how much money do you have saved under your mattress? "))
bank_savings = float(input(name + ", how much money do you have saved in your bank? "))
bonds = float(input(name + ", how much money do you have saved in bonds? "))
stocks = float(input(name + ", how much money do you have saved in stocks? "))

current_age = int(input(name + ", how old are you?"))
retirement_age = int(input(name + ", how old do you want to be when you retire?"))

years_until_retirement = retirement_age - current_age

bank_savings *= 1.01**years_until_retirement
bonds *= 1.02**years_until_retirement
stocks *= 1.1**years_until_retirement

print(f"{name}, when you retire, your money under the mattress will be worth: ${money_under_the_mattress:,.2f}")
print(f"{name}, when you retire, your money in bank savings will be worth: ${bank_savings:,.2f}")
print(f"{name}, when you retire, your money in bonds will be worth: ${bonds:,.2f}")
print(f"{name}, when you retire, your money in stocks will be worth: ${stocks:,.2f}")

total_savings = money_under_the_mattress + bank_savings + bonds + stocks

print(f"{name}, when you retire, your total savings will be worth: ${total_savings:,.2f}")

total_savings /= 1.03**years_until_retirement

print(f"{name}, the present value of your savings is worth: ${total_savings:,.2f}")
