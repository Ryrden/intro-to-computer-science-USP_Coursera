def n_primos(k):
    while k < 2:
        print("valor inválido!!")
        return None
    if k != 2:
        x = k - 1 
    else:
        x = k
    
    é_primo = 0
    while x > 1:
        i = 1 
        np = 0 
        while i <= x:
            z = x % i
            if z == 0: 
                np = np + 1
            i = i + 1

        if np <= 2:
            é_primo = é_primo + 1 
        x = x - 1
    return é_primo

