count = 0
def fibonacci(n):
    global count
    count = count + 1
    if not isinstance(n, int):
        print ('Invalid Input')
        return None

    if n < 0:
        print ('Invalid Input')
        return None
        
    if n == 0:
        return 0

    if n == 1:
        return 1

    fib = fibonacci(n-1) + fibonacci(n-2)
    return fib

fibonacci(-5)
print(count)