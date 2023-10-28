from datetime import date, timedelta

users = [
    {"name": "Marta", "birthday": date(1994, 4, 23)},
    {"name": "Magdalena", "birthday": date(1994, 7, 8)},
    {"name": "Milena", "birthday": date(1994, 7, 19)},
    {"name": "Paulina", "birthday": date(1994, 3, 7)},
    {"name": "Justyna", "birthday": date(1995, 10, 29)},
    {"name": "Marcin", "birthday": date(1994, 11, 4)},
]


def get_birthday_per_week(users):

    today = date.today()

    tomorrow = today + timedelta(days=1)

    day_after_week = today + timedelta(days=7)

    birthday_dict = {i: [] for i in range(7)}

    for user in users:
        if tomorrow.timetuple()[1:3] <= user["birthday"].timetuple()[1:3] and day_after_week.timetuple()[1:3] >= user["birthday"].timetuple()[1:3]:
            day_of_week = user["birthday"].weekday()
            birthday_dict[day_of_week].append(user["name"])

    days_of_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]

    for day, names in birthday_dict.items():
        if names:
            if day in [5, 6]:  # 5 to sobota, 6 to niedziela
                print(f"Monday: {', '.join(names)}")
            else:
                print(f"{days_of_week[day]}: {', '.join(names)}")


get_birthday_per_week(users)
