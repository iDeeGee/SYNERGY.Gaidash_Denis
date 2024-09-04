# Задание 1:

def CreateFactorialList():
    number = int(input("Введите натуральное число: "))
    
    result = 1
    factorials = []
    
    for i in range(2, number + 1):
        result *= i
    
    for i in range(number, 0, -1):
        factorials.append(result)
        result //= i  
    
    return factorials

resulting_list = CreateFactorialList()
print(resulting_list)

# Задание 2:
pets = {}

# инфо id
def get_pet(ID):
    return pets.get(ID, False)

# получение суф возраста
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"

# создание записи
def create():
    new_id = max(pets.keys(), default=0) + 1

    while True:
        pet_name = input("Введите имя питомца: ").strip()
        if pet_name:
            break
        print("Строка не может быть пустой")

    while True:
        pet_type = input("Введите вид питомца: ").strip()
        if pet_type:
            break
        print("Строка не может быть пустой")

    while True:
        pet_age_str = input("Введите возраст питомца: ").strip()
        if pet_age_str.isdigit():
            pet_age = int(pet_age_str)
            break
        print("Возраст должен быть числом и не может быть пустым")

    while True:
        owner_name = input("Введите имя владельца: ").strip()
        if owner_name:
            break
        print("Строка не может быть пустой")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец {pet_name} добавлен с ID {new_id}.")

# инфо питомца 
def read():
    while True:
        ID_str = input("Введите ID питомца для просмотра информации: ").strip()
        if ID_str.isdigit():
            ID = int(ID_str)
            break
        print("ID должен быть числом и не может быть пустым")

    pet = get_pet(ID)
    if pet:
        for name, details in pet.items():
            suffix = get_suffix(details["Возраст питомца"])
            print(f'Это {details["Вид питомца"]} по кличке "{name}".\n'
                  f'Возраст питомца: {details["Возраст питомца"]} {suffix}.\n'
                  f'Имя владельца: {details["Имя владельца"]}\n')
    else:
        print(f"Питомец с ID {ID} не найден.")

# обновление 
def update():
    while True:
        ID_str = input("Введите ID питомца для обновления информации: ").strip()
        if ID_str.isdigit():
            ID = int(ID_str)
            break
        print("ID должен быть числом и не может быть пустым")

    pet = get_pet(ID)
    if pet:
        for name, details in pet.items():
            print(f"Текущая информация: {details}")
            species = input(f"Введите новый вид питомца (или нажмите Enter, чтобы оставить '{details['Вид питомца']}'): ").strip() or details["Вид питомца"]
            age_str = input(f"Введите новый возраст питомца (или нажмите Enter, чтобы оставить '{details['Возраст питомца']}'): ").strip()
            age = int(age_str) if age_str.isdigit() else details["Возраст питомца"]
            owner = input(f"Введите новое имя владельца (или нажмите Enter, чтобы оставить '{details['Имя владельца']}'): ").strip() or details["Имя владельца"]

            details["Вид питомца"] = species
            details["Возраст питомца"] = age
            details["Имя владельца"] = owner

            print(f"Информация о питомце '{name}' обновлена.")
    else:
        print(f"Питомец с ID {ID} не найден.")

# удаление 
def delete():
    while True:
        ID_str = input("Введите ID питомца для удаления: ").strip()
        if ID_str.isdigit():
            ID = int(ID_str)
            break
        print("ID должен быть числом и не может быть пустым")

    pet = get_pet(ID)
    if pet:
        pets.pop(ID)
        print(f"Питомец с ID {ID} удален.")
    else:
        print(f"Питомец с ID {ID} не найден.")

# список
def pets_list():
    if not pets:
        print("Список питомцев пуст.")
    else:
        for ID, pet_info in pets.items():
            for name, details in pet_info.items():
                suffix = get_suffix(details["Возраст питомца"])
                print(f'{ID}: Это {details["Вид питомца"]} по кличке "{name}".\n'
                      f'Возраст питомца: {details["Возраст питомца"]} {suffix}.\n'
                      f'Имя владельца: {details["Имя владельца"]}')

# программа
def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
        if not command:
            print("Строка не может быть пустой")
            continue
        if command == "stop":
            break
        elif command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()