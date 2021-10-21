import random

def get_users_name():
    name = input("What's your name human? ")
    return name


def get_initial_money_for_account_type(account_type):
    initial_balance = int(input(f"How much money do you currently have saved/invested in your {account_type}? "))
    return initial_balance


def get_current_age_and_retirement_age():
    current_age = int(input("How old are you?"))
    retirement_age = int(input("What age do you want to retire?"))
    return current_age, retirement_age


def do_you_want_to_add_more_money_this_year(current_age):
    answer = input(f"Do you want to add more money to your accounts at age {current_age}? (y/n)")
    return answer


def what_asset_type():
    asset_type = ""
    while asset_type not in ('mattress', 'bank savings', 'bonds', 'stocks'):
        asset_type = input("What account do you want to add more to? mattress, bank savings, bonds, or stocks?")
    return asset_type


def ask_how_much_to_add_money_to_asset_type(asset_type):
    money_to_add = int(input(f"How much money did you want to add to your {asset_type}? "))
    return money_to_add


def add_to_asset_type(asset_type, how_much_to_add, mattress_money, bank_savings, bonds_savings, stocks):
    if asset_type == 'mattress':
        mattress_money += how_much_to_add
    elif asset_type == 'bank savings':
        bank_savings += how_much_to_add
    elif asset_type == 'bonds':
        bonds_savings += how_much_to_add
    elif asset_type == 'stocks':
        stocks += how_much_to_add
    return mattress_money, bank_savings, bonds_savings, stocks


def ask_what_asset_and_how_much_to_add(mattress_money, bank_savings, bonds_savings, stocks):
    pass


def add_return_on_investment(bank_savings, bonds_savings, stocks):
    bank_savings += bank_savings * .01
    bonds_savings += bonds_savings * random.randint(1,5) / 100
    stocks += stocks * random.randint(-10, 20) / 200
    return bank_savings, bonds_savings, stocks


def calculate_present_value(age, retirement_age, total_value):
    return total_value / 1.03**(retirement_age - age)


name = get_users_name()

mattress_money = get_initial_money_for_account_type("mattress")
bank_savings = get_initial_money_for_account_type("bank savings")
bonds_savings = get_initial_money_for_account_type("bonds")
stocks = get_initial_money_for_account_type("stocks")

age, retirement_age = get_current_age_and_retirement_age()

current_age = age
while current_age < retirement_age:
    add_more_this_year = do_you_want_to_add_more_money_this_year(current_age)
    while add_more_this_year.lower() == "y":
        asset_type = what_asset_type()
        how_much_to_add = ask_how_much_to_add_money_to_asset_type(asset_type)
        mattress_money, bank_savings, bonds_savings, stocks = add_to_asset_type(asset_type, how_much_to_add, mattress_money, bank_savings, bonds_savings, stocks)

        # instead of 3 different methods, do all of it at once
        # mattress_money, bank_savings, bonds_savings, stocks = ask_what_asset_and_how_much_to_add(mattress_money, bank_savings, bonds_savings, stocks)

        add_more_this_year = do_you_want_to_add_more_money_this_year(current_age)

    #mattress money don't have a return on investment
    bank_savings, bonds_savings, stocks = add_return_on_investment(bank_savings, bonds_savings, stocks)
    current_age += 1

total_value = mattress_money + bank_savings + bonds_savings + stocks

print(f"Total value of mattress  {mattress_money:.2f}")
print(f"Total value of bank savings  {bank_savings:.2f}")
print(f"Total value of bonds  {bonds_savings:.2f}")
print(f"Total value of stocks  {stocks:.2f}")
print(f"Total value at retirement age {total_value:.2f}")

present_value = calculate_present_value(age, retirement_age, total_value)
print(f"Value in today's dollars: {present_value:.2f}")


