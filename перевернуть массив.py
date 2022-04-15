a = [1, 2, 3, 45, 89, 74, 64, 2222, 555, 94, 4, 4444444444, 54]

b = []
for index in range(len(a), 0, -1):
    b.append(a[index - 1])
print(b)

# альтернативные варианты:
# b = a [::-1]
# print(b)


# for i in reversed (a):
#    print(i)
