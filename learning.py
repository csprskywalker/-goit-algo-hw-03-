from datetime import datetime
import random

#task 1
def get_days_from_today(date):
    try:
        dates = datetime.strptime(date, "%Y-%m-%d")
        date_today = datetime.today()
        result = (date_today - dates).days
        return result
    except ValueError:
        print("Invalid input. Corrent input option YYYY-MM-DD")

#task 2
def get_numbers_ticket(min, max, quantity):
    try:
        min, max, quantity = int(min), int(max), int(quantity)

        if not 1 <= min != max <= 1000:
            raise ValueError("Min and max must be in the range 1-1000, where min != max.")
        if quantity < 1 or quantity > (max - min + 1):
            raise ValueError("Quantity must be at least 1 and no more than the number of numbers in the range.")

        #main
        random_number = sorted([random.randint(min, max) for _ in range(quantity)])
        return random_number


    except ValueError as e:
        return f"Value Error: {str(e)}"
    except TypeError as e:
        return f"Type Error: {str(e)}"

print(get_days_from_today("2024-4-10"))
print(get_numbers_ticket(1, 500, 10))
print(get_numbers_ticket(500, 500, 5))
print(get_numbers_ticket(123, 456, 5))
#end
