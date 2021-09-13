def fibonacci(n):

    if n <= 2:  # Base da recursão
        return 1

    return fibonacci(n-1) + fibonacci(n-2) # Chamada da recursão
