# Задание 1:
N = int(input("Введите количество чисел N: "))

if not (1 <= N <= 100000):
    raise ValueError("N должно быть в диапазоне от 1 до 100000")

input_numbers = input("Введите N чисел через пробел: ").split()

if len(input_numbers) != N:
    raise ValueError("Количество введенных чисел должно совпадать с N")

unique_numbers = set()

for num_str in input_numbers:
    num = int(num_str)
    if abs(num) > 2 * 10**10:
        raise ValueError("Недопустимое значение!")
    unique_numbers.add(num)

print("Количество уникальных чисел: ", len(unique_numbers))

# Задание 2:
num_list_1 = int(input("Введите количество числел в первом списке: "))
if not (num_list_1 <= 100000):
    raise ValueError("Недопустимые значения!")

list_1 = set()

for _ in range(num_list_1):
    num = int(input())
    list_1.add(num)

num_list_2 = int(input("Введите количество числел во втором списке: "))
if not (num_list_2 <= 100000):
    raise ValueError("Недопустимые значения!")

list_2 = set()

for _ in range(num_list_2):
    num = int(input())
    list_2.add(num)

print("Количество дубликатов: ", len(list_1.intersection(list_2)))

# Задание 3:
number=set()

for num in input().split():

    if num not in number:
        number.add(num)
        print('NO')
    else:
        print('YES')