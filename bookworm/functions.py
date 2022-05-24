fib_arr = [0, 1]
 
def fibonacci(n):
    try:
        if n < len(fib_arr):
            return fib_arr[n]
        else:       
            fib_arr.append(fibonacci(n - 1) + fibonacci(n - 2))
            return fib_arr[n]
    except Exception as e:
        return(e)
