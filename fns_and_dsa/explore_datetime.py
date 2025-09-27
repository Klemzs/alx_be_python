from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

def calculate_future_date():
    current_date = display_current_datetime()
    number_of_days = int(input("Enter number of days: "))
    future_date = current_date + datetime.timedelta(days = number_of_days)
    return future_date

print(f"Current date and time: {display_current_datetime()}")
print(f"future date: {calculate_future_date()}")
