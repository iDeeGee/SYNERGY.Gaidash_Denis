# Задание 1:
side_a = float(input("Введите сторону a: "))
side_b = float(input("Введите сторону b: "))

square = side_a * side_b
perimeter = (side_a + side_b) * 2

print(f"Периметр прямоугольника = {perimeter}\nПлощадь прямоугольника = {square}")

# Задание 2:
number = (input("Введите пятизначное целое число: "))
unit = float(number[-1])
dozen = float(number[-2])
hundred = float(number[-3])
thousand = float(number[-4])
ten_of_thousand = float(number[-5])

result = (dozen ** unit) * hundred // (ten_of_thousand - thousand)
print(result)