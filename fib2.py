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

    a = 2 
    b = 1 
    for c in range(0,n):
        a = b
        b = count
        count = a + b
            
fibonacci(306)
print(count)