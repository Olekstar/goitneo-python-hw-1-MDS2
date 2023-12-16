from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_next_week(users):
    # Збереження дня народження в словник
    birthdays_by_day = defaultdict(list)

    # Отримання поточної дати
    today = datetime.today().date()

    # Пошук першого понеділка наступного тижня
    next_monday = today + timedelta(days=(7 - today.weekday()))

    # Цикл for для проходу по всім користувачам
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Конвертація дня народження до типу date, видаляючи часову частину
        birthday_this_year = birthday.replace(year=today.year)

        # Перевірка, чи день народження наступає на наступному тижні
        if next_monday <= birthday_this_year <= next_monday + timedelta(days=6):
            # Визначення дня тижня дня народження
            day_of_week = birthday_this_year.strftime("%A")

            # Якщо день народження вихідний, привітати в понеділок
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"

            # Збереження імені користувача в відповідний день тижня
            birthdays_by_day[day_of_week].append(name)

    # Виведення результату
    print("Our birthday guys this week:")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in weekdays:
        names = birthdays_by_day[day]
        if names:
            print(f"{day}: {', '.join(names)}")


# Приклад використання
users = [
    {"name": "Anna", "birthday": datetime(1981, 12, 27)},
    {"name": "Ivan", "birthday": datetime(1982, 12, 26)},
    {"name": "Maria", "birthday": datetime(2001, 12, 25)},
    {"name": "Petro", "birthday": datetime(2002, 12, 24)},
    {"name": "Olga", "birthday": datetime(2002, 12, 23)},
    {"name": "Sergiy", "birthday": datetime(2003, 12, 22)},
    {"name": "Viktoriya", "birthday": datetime(2004, 12, 21)},
    {"name": "Oleksandr", "birthday": datetime(2001, 12, 20)},
    {"name": "Kateryna", "birthday": datetime(2001, 12, 19)},
    {"name": "Dmytro", "birthday": datetime(2001, 12, 18)},
    {"name": "Maryna", "birthday": datetime(2001, 12, 17)},
    {"name": "Pavlo", "birthday": datetime(2001, 12, 16)},
]

get_birthdays_next_week(users)