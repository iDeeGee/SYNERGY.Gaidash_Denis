# Задание 1:
number = int(input("Введите целое число: "))
if (number % 2 == 0) and (number > 0):
    print(f"{number} - Положительное четное число")
elif (number % 2 == 0) and (number < 0):
    print(f"{number} - Отрицательное четное число")
elif (number % 2 != 0) and (number > 0):
    print(f"{number} - Положительное нечетное число")    
elif (number % 2 != 0) and (number < 0):
    print(f"{number} - Отрицательное нечетное число")
elif number == 0:
    print(f"{number} - Нулевое число")


# Задание 2:
word = (input("Введите слово латинскими буквами: ")).lower()

a_count = word.count("a")
e_count = word.count("e")
i_count = word.count("i")
o_count = word.count("o")
u_count = word.count("u")

sum_vowels = a_count + e_count + i_count + o_count + u_count
sum_consonants = len(word) - sum_vowels

print(f"В слове {word}, {sum_vowels} гласных букв и {sum_consonants} согласных букв")

print("Количество каждой гласной буквы: ")

if a_count == 0:
    print("a = Fasle")
else:
    print("a = ", a_count)

if e_count == 0:
    print("e = Fasle")
else:
    print("e = ", e_count)

if i_count == 0:
    print("i = Fasle")
else:
    print("i = ", i_count)     

if o_count == 0:
    print("o = Fasle")
else:
    print("o = ", o_count)

if u_count == 0:
    print("u = Fasle")
else:
    print("u = ", u_count)   

 
 # Задание 3:      
sum_invest = float(input("Введите минимальную сумму для инвестиций: ")) 
wallet_Mike = float(input("Введите сколько долларов у Майкла: "))
wallet_Ivan = float(input("Введите сколько долларов у Ивана: "))

if (wallet_Mike >= sum_invest) and (wallet_Ivan >= sum_invest):
    print("2")
elif (wallet_Mike >= sum_invest) and (wallet_Ivan < sum_invest):
    print("Mike")
elif (wallet_Mike < sum_invest) and (wallet_Ivan >= sum_invest):
    print("Ivan")
elif (wallet_Mike < sum_invest) and (wallet_Ivan < sum_invest) and ((wallet_Mike + wallet_Ivan) >= sum_invest):
    print("1")
elif (wallet_Mike < sum_invest) and (wallet_Ivan < sum_invest) and ((wallet_Mike + wallet_Ivan) < sum_invest):
    print("0")





    