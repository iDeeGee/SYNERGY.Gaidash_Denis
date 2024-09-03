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

# инфо по id
def get_pet(ID):
    return pets.get(ID, False)

# возраст
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"

# созданиt новой записи
def create():
    new_id = max(pets.keys(), default=0) + 1
    
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    
    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"Питомец {pet_name} добавлен с ID {new_id}.")

# отображние инфо по id
def read():
    ID = int(input("Введите ID питомца для просмотра информации: "))
    pet = get_pet(ID)
    if pet:
        for name, details in pet.items():
            suffix = get_suffix(details["Возраст питомца"])
            print(f'Это {details["Вид питомца"]} по кличке "{name}". Возраст питомца: {details["Возраст питомца"]} {suffix}. Имя владельца: {details["Имя владельца"]}')
    else:
        print(f"Питомец с ID {ID} не найден.")

# обновление инфо
def update():
    ID = int(input("Введите ID питомца для обновления информации: "))
    pet = get_pet(ID)
    if pet:
        for name, details in pet.items():
            print(f"Текущая информация: {details}")
            species = input(f"Введите новый вид питомца (или нажмите Enter, чтобы оставить '{details['Вид питомца']}'): ") or details["Вид питомца"]
            age = input(f"Введите новый возраст питомца (или нажмите Enter, чтобы оставить '{details['Возраст питомца']}'): ") or details["Возраст питомца"]
            owner = input(f"Введите новое имя владельца (или нажмите Enter, чтобы оставить '{details['Имя владельца']}'): ") or details["Имя владельца"]

            details["Вид питомца"] = species
            details["Возраст питомца"] = int(age)
            details["Имя владельца"] = owner

            print(f"Информация о питомце '{name}' обновлена.")
    else:
        print(f"Питомец с ID {ID} не найден.")

# удаление записи 
def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    pet = get_pet(ID)
    if pet:
        pets.pop(ID)
        print(f"Питомец с ID {ID} удален.")
    else:
        print(f"Питомец с ID {ID} не найден.")

# отображение списка 
def pets_list():
    for ID, pet_info in pets.items():
        for name, details in pet_info.items():
            suffix = get_suffix(details["Возраст питомца"])
            print(f'{ID}: Это {details["Вид питомца"]} по кличке "{name}". Возраст питомца: {details["Возраст питомца"]} {suffix}. Имя владельца: {details["Имя владельца"]}')

# программа
def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
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
