def parse_input(user_input):
    # Розділення введеного рядка на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    # Додавання контакту
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."
    else:
        return "Невірна команда. Використовуйте: add <ім'я> <телефон>"

def list_contacts(contacts):
    # Виведення усіх контактів
    if not contacts:
        return "Контактів не знайдено."
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def save_contacts(contacts, filename="contacts.txt"):
    # Збереження контактів у файл
    with open(filename, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

def change_contact(args, contacts):
    # Зміна номера телефону для заданого імені
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"Номер телефону для {name} змінено на {new_phone}."
        else:
            return f"Контакт з ім'ям {name} не знайдено."
    else:
        return "Невірна команда. Використовуйте: change <ім'я> <новий_телефон>"

def load_contacts(filename="contacts.txt"):
    # Завантаження контактів з файлу
    contacts = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone = line.strip().split(":")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def main():
    # Основна функція бота
    contacts = load_contacts()
    print("Ласкаво просимо до бота-асистента!")
    
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_contacts(contacts)
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
