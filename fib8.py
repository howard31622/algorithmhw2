import numpy as np
count = 0
def fibonacci(n,k):
    global count
    if not isinstance(n, int):
        print ('Invalid Input')
        return None
    if n < 0:
        print ('Invalid Input')
        return None
    if n < k:
        print ('Invalid Input')
        return None

    x = np.zeros(k)   
    x[k-1] = 1
    y = np.zeros(n+1)
    for a in range(0,n+1):
        if a<k:
            y[a] = x[a]
        else:
            for b in range(a-k,a):
                y[a] = y[a]+y[b]
    count = int(y[n])
    

fibonacci(12,4)
print(count)