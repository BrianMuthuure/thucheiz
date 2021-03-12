import datetime
import calendar
"""
months that will take to pay off a credit card
"""
balance = 5000
interest_rate = 13 * .01
monthly_payment = 1000

today = datetime.date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1]  # get only the days in the month
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge  # same as balance = balance + interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)  # Round balance to 2 decimal places
    if balance < 0:  # To get a non-negative balance
        balance = 0
    # balance = 0 if balance < 0 else round(balance, 2)  # set balance=0 if its negative ....else set balance and round
    print(end_date, balance)
    # Incrementing over to the next month
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]  # get only the days in the month

    end_date = end_date + datetime.timedelta(days=days_in_current_month)