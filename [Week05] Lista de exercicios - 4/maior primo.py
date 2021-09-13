def éPrimo(x):  #Verifica Primo
    i = 1 
    np = 0 #np = não primo

    while i <= x:
        z = x % i
        if z == 0: 
            np = np + 1
        i = i + 1
    if np > 2:
        return False    #não é primo
    else:
        return True     #é primo

def maior_primo(z):  # Qual o maior primo até o número digitado
    x = z
    k = éPrimo(x)

    if k == False: 
        while not éPrimo(x) == True:
            k = éPrimo(x)
            if éPrimo == True:
                return x
            x = x - 1
        return x
    else:        #se verdadeiro
        return x