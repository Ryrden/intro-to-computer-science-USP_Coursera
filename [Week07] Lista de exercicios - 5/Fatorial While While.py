x = int(input("Quantos fatoriais diferentes você quer saber? "))

while x > 0:
    k = int(input("Fatorial de: "))
    fat = k
    while k > 1:
        fat = fat * (k-1)
        k = k - 1
    if fat == 0:
        fat = 1
    print("vale: ",fat)
    x = x - 1
