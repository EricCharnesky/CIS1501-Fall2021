def number_of_payments(annual_rate, monthly_payment_amount, loan_amount):

    if annual_rate < 0 or annual_rate >= 1:
        raise ValueError("Annual rate must be between 0 and 1")

    if loan_amount <= 0:
        raise ValueError("Loan amount must be > 0")

    loan_balance = loan_amount
    payments = 0

    while loan_balance > 0:
        payments += 1

        loan_balance += loan_balance * annual_rate / 12
        loan_balance -= monthly_payment_amount

    return payments


def payment_amount(annual_rate, payments, loan_amount):

    if annual_rate < 0 or annual_rate >= 1:
        raise ValueError("Annual rate must be between 0 and 1")

    if loan_amount <= 0:
        raise ValueError("Loan amount must be > 0")

    monthly_rate = annual_rate / 12
    payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate)**-payments))

    return payment

