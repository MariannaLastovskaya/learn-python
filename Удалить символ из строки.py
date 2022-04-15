string = "Hello developers!I love Python!"

#выводим в консоль исходную строку

print ("Исходная строка: " + string)
result_str = ""
for i in range (0, len(string)):
    if i != 3:
        result_str = result_str + string[i]

#выводим в консоль строку после удаления i-го элемента

print("Cтрока после удаления i-го элемента: " + result_str)
