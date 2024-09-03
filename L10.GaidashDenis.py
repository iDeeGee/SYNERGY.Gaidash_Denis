# Задание 1:
pets = {}
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

if pet_age % 10 == 1 and pet_age % 100 != 11:
    age_word = "год"
elif 2 <= pet_age % 10 <= 4 and not (12 <= pet_age % 100 <= 14):
    age_word = "года"
else:
    age_word = "лет"

for name, details in pets.items():
    pet_type = details['Вид питомца']
    pet_age = details['Возраст питомца']
    owner_name = details['Имя владельца']
    
    print(f"Это {pet_type} по кличке \"{name}\". Возраст питомца: {pet_age} {age_word}. Имя владельца: {owner_name}.")



# Задание 2:
extent_dict = {}

for i in range(10, -6, -1):
    extent_dict[i] = i ** i  
    print(f"{i} : {extent_dict[i]}")

#print(extent_dict)    




