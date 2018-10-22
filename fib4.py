import cmath
import math
count = 0
def fibonacci(n):
    global count
    #count = count + 1
    if not isinstance(n, int):
        print ('Invalid Input')
        return None
    if n < 0:
        print ('Invalid Input')
        return None

    count = math.pow(((1+(cmath.sqrt(5).real))/2), n/2 )*math.pow(((1+(cmath.sqrt(5).real))/2), n/2 )

fibonacci(2)
print(count)