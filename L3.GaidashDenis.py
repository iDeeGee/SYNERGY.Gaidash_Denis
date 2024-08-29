# Задание 1:
type = input("Введите вид питомца: ")
age = input("Его возраст: ")
nickname = input ("Проивище: ")

print(f'Это {type} по кличке "{nickname}". Возраст: {age} года/лет')

# Задание 2:
quest_1 = input("Введите первый этап развития человека: ")
quest_2 = input("Введите второй этап развития человека: ")
quest_3 = input("Введите третий этап развития человека: ")
quest_4 = input("Введите четвёртый этап развития человека: ")
quest_5 = input("Введите пятый этап развития человека: ")
quest_6 = input("Введите последний этап развития человека: ")

stadia_1 = "Australopithecus"
stadia_2 = "Homo habilis"
stadia_3 = "Homo erectus"
stadia_4 = "Homo sapiens"
stadia_5 = "Homo neanderthalensis"
stadia_6 = "Homo sapiens sapiens"

print("\nВаша цепочка ответов: ")
print(quest_1, quest_2, quest_3, quest_4, quest_5, quest_6, sep = "=>")
print("\nПравильный вариант цепочки: ")
print(stadia_1, stadia_2, stadia_3, stadia_4, stadia_5, stadia_6, sep = "=>")