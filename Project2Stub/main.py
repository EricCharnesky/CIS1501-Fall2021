
def get_users_name():
    pass
    # pass means I know it's empty, I'll come back to it


def get_initial_money_for_account_type(account_type):
    pass


def get_current_age_and_retirement_age():
    pass


def do_you_want_to_add_more_money_this_year(current_age):
    pass


def what_asset_type():
    pass


def ask_how_much_to_add_money_to_asset_type(asset_type):
    pass


def add_to_asset_type(asset_type, how_much_to_add, mattress_money, bank_savings, bonds_savings, stocks):
    pass


def ask_what_asset_and_how_much_to_add(mattress_money, bank_savings, bonds_savings, stocks):
    pass


def add_return_on_investment(bank_savings, bonds_savings, stocks):
    pass


def calculate_present_value(age, retirement_age, total_value):
    pass


name = get_users_name()

mattress_money = get_initial_money_for_account_type("mattress")
bank_savings = get_initial_money_for_account_type("bank savings")
bonds_savings = get_initial_money_for_account_type("bonds")
stocks = get_initial_money_for_account_type("stocks")

age, retirement_age = get_current_age_and_retirement_age()

current_age = age
while current_age < retirement_age:
    add_more_this_year = do_you_want_to_add_more_money_this_year(current_age)
    while add_more_this_year == "y":
        asset_type = what_asset_type()
        how_much_to_add = ask_how_much_to_add_money_to_asset_type(asset_type)
        mattress_money, bank_savings, bonds_savings, stocks = add_to_asset_type(asset_type, how_much_to_add, mattress_money, bank_savings, bonds_savings, stocks)

        # instead of 3 different methods, do all of it at once
        # mattress_money, bank_savings, bonds_savings, stocks = ask_what_asset_and_how_much_to_add(mattress_money, bank_savings, bonds_savings, stocks)

        add_more_this_year = do_you_want_to_add_more_money_this_year(current_age)

    #mattress money don't have a return on investment
    bank_savings, bonds_savings, stocks = add_return_on_investment(bank_savings, bonds_savings, stocks)

total_value = mattress_money + bank_savings + bonds_savings + stocks

print("values at retirement age...")

present_value = calculate_present_value(age, retirement_age, total_value)

