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
    {"name": "Anna", "birthday": datetime(1981, 1, 1)},
    {"name": "Ivan", "birthday": datetime(1982, 2, 2)},
    {"name": "Maria", "birthday": datetime(2001, 3, 3)},
    {"name": "Petro", "birthday": datetime(2002, 4, 4)},
    {"name": "Olga", "birthday": datetime(2002, 5, 5)},
    {"name": "Sergiy", "birthday": datetime(2003, 6, 6)},
    {"name": "Viktoriya", "birthday": datetime(2004, 7, 7)},
    {"name": "Oleksandr", "birthday": datetime(2001, 8, 8)},
    {"name": "Kateryna", "birthday": datetime(2001, 12, 9)},
    {"name": "Dmytro", "birthday": datetime(2001, 12, 9)},
    {"name": "Maryna", "birthday": datetime(2001, 12, 7)},
    {"name": "Pavlo", "birthday": datetime(2001, 12, 6)},
]

get_birthdays_next_week(users)
