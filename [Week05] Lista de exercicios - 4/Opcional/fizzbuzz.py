def fizzbuzz(x):
    t = x % 3 #divisivel por 3
    c = x % 5 #divisivel por 5

    if t == 0 and c == 0:
        return "FizzBuzz"
    elif t == 0:
        return "Fizz"
    elif c == 0:
        return "Buzz"
    else:
        return x