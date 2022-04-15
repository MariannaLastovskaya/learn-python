string = "Hello developers!I love Python!"
index = string.find("Python")
print(index)

# ищем с десятого индекса
index = string.find("Python", 10)
print(index)  # 21

# ищем с 10-го по 15-й индекс
index = string.find("Python", 10, 15)
print(index)  # -1 когда подстрока не найдена
