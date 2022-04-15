a = [1, 2, 3, 45, 89, 74, 64, 2222, 555, 94, 4, 4444444444, 54]

for run in range(len(a) - 1):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp

print(a)
