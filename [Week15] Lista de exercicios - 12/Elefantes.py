def incomodam(n):

    if n == 1:
        return 'incomodam '

    if n <= 0:
        return ''
    return 'incomodam ' + incomodam(n-1)


def elefantes(n, cont=1):

    if n <= 1:
        return ''
    if cont == 1:
        return "Um elefante incomoda muita gente\n" + elefantes(n, cont+1)
    if n == 2:
        return str(cont) + ' elefantes ' + incomodam(cont) + "muito mais" + '\n' + elefantes(n-1, cont+1)

    return str(cont) + ' elefantes ' + incomodam(cont) + "muito mais" + '\n' + str(cont) + ' elefantes incomodam muita gente\n' + elefantes(n-1, cont+1)

