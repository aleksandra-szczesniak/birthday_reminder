from datetime import date

users = [
    {"name": "Marta", "birthday": date(1994, 11, 11)},
    {"name": "Magdalena", "birthday": date(1994, 11, 12)},
    {"name": "Milena", "birthday": date(1994, 11, 4)},
    {"name": "Paulina", "birthday": date(1994, 11, 5)},
    {"name": "Justyna", "birthday": date(1995, 11, 6)},
    {"name": "Marcin", "birthday": date(1994, 11, 9)},
]


def get_birthday_per_week(users):
    today = date.today()
    birthday_dict = {i: [] for i in range(5)}

    for user in users:
        days_until_birthday = (user["birthday"].replace(
            year=today.year) - today).days
        if 0 <= days_until_birthday < 7:
            day_of_week = (today.weekday() + days_until_birthday) % 7
            if day_of_week >= 5:
                days_until_birthday += (7 - day_of_week)
                day_of_week = 0

            if days_until_birthday < 7:
                birthday_dict[day_of_week].append(user["name"])

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for day, names in birthday_dict.items():
        if names:
            print(f"{days_of_week[day]}: {', '.join(names)}")


get_birthday_per_week(users)
