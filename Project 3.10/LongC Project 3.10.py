print("This program will display a payment plan for your loan.")
p_price = float(input("Please enter the purchase price: "))

interest_rate = .12
down_payment = p_price * 0.1
starting_bal = p_price - down_payment
ending_bal = p_price - down_payment
monthly_payment = starting_bal * .05
month = 1
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
while ending_bal > 0:
    if starting_bal < monthly_payment:
        monthly_payment = 0
        monthly_payment += starting_bal
        monthly_principal = monthly_payment
        monthly_interest = 0
    else:
        monthly_interest = starting_bal * interest_rate / 12
        monthly_principal = monthly_payment - monthly_interest
    ending_bal = (starting_bal - monthly_payment) + monthly_interest
    print("%2d%15.2f%15.2f%18.2f%15.2f%15.2f" % (month, starting_bal, monthly_interest, monthly_principal, monthly_payment, ending_bal))
    starting_bal = ending_bal
    month += 1   
else:
    print("Completed")
    input()