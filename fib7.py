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
    if n == 0 :
        count = 2
        return count
    if n == 1:
        count = 1
        return count     

    a = 2 
    b = 1 
    for c in range(0,n):
        a = b
        b = count
        count = a + b
            
fibonacci(3)
print(count)