import numpy as np
count = np.array([[1,1],[1,0]])
def fibonacci(n):
    global count
    if not isinstance(n, int):
        print ('Invalid Input')
        return None
    if n < 0:
        print ('Invalid Input')
        return None
    A = np.array([[1,1],[1,0]])
    for a in range(1,n):
   		count = np.dot(count,A)
   	
fibonacci(5)
print (count[0][0])