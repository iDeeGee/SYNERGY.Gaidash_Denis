# Задание 1:
N = int(input("Введите количество чисел N: "))
numbers = []

for _ in range(N):
    number = int(input())
    numbers.append(number)

reversed_numbers = numbers[::-1]
print(" ".join(map(str, reversed_numbers)))

# Задание 2:
num_N = int(input("Введите количество чисел N: "))
array = list(map(int, input("Введите N чисел через пробел: ").split()))

rearranged_array = [0] * num_N

for i in range(num_N):
    if i % 2 == 0:
        rearranged_array[i] = array[-(i//2 + 1)]
    else:
        rearranged_array[i] = array[i//2]

print(" ".join(map(str, rearranged_array)))

# Задание 3:
m = int(input("Введите максимальную массу, которую может выдержать лодка: "))
n = int(input("Введите количество рыбаков: "))

weights = []
for _ in range(n):
    weights.append(int(input()))

weights.sort()

left = 0  
right = n - 1  
boats = 0 

while left <= right:
    
    if weights[left] + weights[right] <= m:
        left += 1  
    
    right -= 1  
    boats += 1 

print(boats)