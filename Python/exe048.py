s = 0
for c in range(0,501,3):
    impar = c%2
    if impar == 1:
        s += c
        print(c)
print(s)