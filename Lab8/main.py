import financial

choice = input("Do you want to calculate the (N)umber of payments or (P)ayment amount?")
if choice.upper() == "N":
    annual_rate = float(input("What is the annual rate 0-1"))
    payment_amount = float(input("What is the payment amount?"))
    loan_amount = float(input("What is the loan amount?"))

    try:
        payments = financial.number_of_payments(annual_rate, payment_amount, loan_amount)
        print(f"It will take {payments} to pay off the loan")
    except ValueError as e:
        print(e)

elif choice.upper() == "P":
    annual_rate = float(input("What is the annual rate 0-1"))
    payments = float(input("How many payments are you making?"))
    loan_amount = float(input("What is the loan amount?"))

    try:
        payment_amount = financial.payment_amount(annual_rate, payments, loan_amount)
        print(f"You will have to pay {payment_amount} monthly")
    except ValueError as e:
        print(e)

else:
    print("I can't do that")