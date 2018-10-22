count = 0
def fibonacci(n):
    global count
    #count = count + 1
    if not isinstance(n, int):
        print ('Invalid Input')
        return None
    if n == 0:
        count = 0
    if n == 1:
        count = 1
    if n < 0:
        a = 0
        b = 1
        for c in range(n,0):
            count = b - a
            b = a
            a = count
    if n > 1:    
        a = 0
        b = 1
        for c in range(0,n):
            a = b
            b = count
            count = a + b
        

fibonacci(-5)
print(count)