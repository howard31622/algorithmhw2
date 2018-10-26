count = 0
def fibonacci(n):
    global count
    if not isinstance(n, int):
        print ('Invalid Input')
        return None
    if n < 0:
        print ('Invalid Input')
        return None
    count = (((1+(5 ** 0.5))/2) ** (n/2)) * (((1+(5 ** 0.5))/2) ** (n/2))
fibonacci(5)
print(count)