def RecursCall(my_list, index=0):
    if index >= len(my_list):
        print("Конец списка")
        return
    print(my_list[index])    
    RecursCall(my_list, index + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

RecursCall(my_list)
