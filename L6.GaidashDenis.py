# Задание 1:
zero_count = 0
for i in range(int(input("Введите число: "))):
    if int(input("Введите числа: ")) == 0:
        zero_count += 1
print(f"Количество чисел равных 0: {zero_count}")


# Задание 2:
nat_number = int(input("Введите натуральное число:"))
count = 0

for divider in range (1, nat_number + 1):
    if nat_number % divider == 0:
        count = count + 1

print(count)


# Задание 3:
num_a = int(input("Введите целое число a: "))
num_b = int(input("Введите целое число b: "))

if num_a >= num_b:
    print("Неверные данные!")
else:
    for number in range(num_a, num_b + 1):
        if number % 2 == 0:
            print(number, end = " ")