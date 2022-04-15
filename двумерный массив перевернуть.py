
a = [[5,6,7],
     [9,8,11]]
b = [[a[j][i] for j in range(len(a))]
     for i in range(len(a[0]))]
print(a)
print(b)



