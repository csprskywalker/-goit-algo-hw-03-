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
            return []
        if quantity < 1 or quantity > (max - min + 1):
            return []
        #main
        random_number = random.sample(range(min, max + 1), quantity)
        sorted_numbers = sorted(random_number)

        return sorted_numbers


    except ValueError as e:
        return f"Value Error: {str(e)}"
    except TypeError as e:
        return f"Type Error: {str(e)}"

print(get_days_from_today("2024-4-10"))
print(get_numbers_ticket(1, 500, 10))
print(get_numbers_ticket(500, 500, 5))

