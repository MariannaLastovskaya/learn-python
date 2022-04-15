# вариант 1
import pandas as pd

string = "Hello developers!I love Python!"
print(pd.Series(list(string)).value_counts())

# вариант 2
string2 = "Hello developers!I love Python!"

count = 0

for i in string2:
    if i == 'l':
        count = count + 1

print(count)

# string = "Hello developers!I love Python!"
# number_of_characters = len(string)
# print('Количество символов в строке:', number_of_characters)
