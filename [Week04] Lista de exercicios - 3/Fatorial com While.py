n = int(input("Digite o valor de n: "))
 
fat = n

if (n != 0):
    while (n > 1):
        fat = fat * (n-1)
        n = n - 1
else:
    fat = 1

print(fat)
