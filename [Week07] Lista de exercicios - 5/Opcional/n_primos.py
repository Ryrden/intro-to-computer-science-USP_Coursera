def is_prime(n):
    div = 2
    while(div < n):
        if n % div == 0:
            return False
        div += 1
    return True

def n_primos(n):
    primos = 0
    while n > 1: 
        if is_prime(n):
            primos += 1
        n -= 1
    return primos
