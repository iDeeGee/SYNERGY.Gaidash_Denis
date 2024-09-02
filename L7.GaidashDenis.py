# Задание 1:
print("Введите строку:")
word = input()

reverse = word[::-1]
if word == reverse:
    print("yes")
else:
    print("no")

#Задание 2: 

string = str(input())   
convert = " ".join(string.split())
print(convert)

