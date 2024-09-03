# Задание 1:
N = int(input("Введите количество чисел N: "))

if not (1 <= N <= 10000):
    raise ValueError("N должно быть в диапазоне от 1 до 10000")

numbers = []

for i in range(N):
    number = int(input(f"Введите число {i + 1}: "))
    
    if abs(number) > 10**6:
        raise ValueError("Недопустимые значения!")
    
    numbers.append(number)

reversed_numbers = numbers[::-1]

print(*reversed_numbers)

# Задание 2:
N = int(input("Введите количество чисел N: "))

if not (1 <= N <= 100000):
    raise ValueError("N должно быть в диапазоне от 1 до 100000")

input_numbers = input("Введите N чисел через пробел: ").split()

if len(input_numbers) != N:
    raise ValueError("Количество введенных чисел должно совпадать с N")

numbers = []
for num_str in input_numbers:
    num = int(num_str)
    if not (1 <= num <= 10**10):
        raise ValueError("Недопустимое значение!")
    numbers.append(num)

rearranged_numbers = [0] * N

for i in range(N):
    if i % 2 == 0:
        rearranged_numbers[i] = numbers[-(i // 2 + 1)]
    else:
        rearranged_numbers[i] = numbers[i // 2]

print(*rearranged_numbers)


# Задание 3:
m = int(input("Введите максимальную массу, которую может выдержать лодка: "))

if not (1 <= m <= 10**7):
    raise ValueError("Недопустимое значение!")

n = int(input("Введите количество рыбаков: "))

if not (1 <= n <= 100):
    raise ValueError("Количество рыбаков должно быть от 1 до 100")

weights = []
for i in range(n):
    weight = int(input(f"Введите вес рыбака {i + 1}: "))
    if not (1 <= weight <= m):
        raise ValueError("Вес рыбака должен быть от 1 до m")
    weights.append(weight)

weights.sort()

boats = 0  
i = 0  
j = n - 1  

while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1  
    
    j -= 1
    boats += 1  

print("Минимальное количество лодок: ", boats)
