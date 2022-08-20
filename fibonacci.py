# Function for nth Fibonacci number
def fibonacci(n):
    # Check if input is a negative number or an invalid type of data
    if n < 0 or isinstance(n, (float, str, list, dict)):
        return -1

    # Check if n is 0 and return 0
    elif n == 0:
        return 0

    # Check if n is 1,2 and return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
