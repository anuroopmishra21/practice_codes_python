def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
