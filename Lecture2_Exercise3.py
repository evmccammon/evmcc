"""
exercise 3 - Design and write a Python
program that calculates your monthly payment based on the number
of hours you work each month and your hourly pay rate

Ask the user to input the number of hours worked and the
hourly pay rate using input().
● Calculate the total monthly payment.
● Print a clear, user-friendly message showing the result using
print() and an f-string.
● E.g., If the user works 10 hours at an hourly rate of 13, the
program should display: Your salary for this month is 130 dollars.

"""
hours_worked = input("Enter the amount of hours worked this month:")
hourly_rate = input("Enter your hourly pay rate:")
monthly_payment = float(hours_worked) * float(hourly_rate)
print(f"Your salary for this month is {monthly_payment} dollars.")