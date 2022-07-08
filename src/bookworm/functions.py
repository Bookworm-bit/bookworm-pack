import time


def fibonacci(n):
    fib_arr = [0, 1]
    try:
        if n < len(fib_arr):
            return fib_arr[n]
        else:
            fib_arr.append(fibonacci(n - 1) + fibonacci(n - 2))
            return fib_arr[n]
    except Exception as e:
        return(e)


def sieve_of_eratosthenes(n):
    numbers = {n: True for n in range(2, n + 1)}

    for item in numbers:
        for number in numbers:
            if number % item == 0 and number > item ** 2:
                numbers[number] = False

    return [number for number in numbers if numbers[number] == True]