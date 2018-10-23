# algorithmhw2

This project is for algorithm homework2

Fibonacii calculation

homework introduction
![image](https://github.com/howard31622/algorithmhw2/blob/master/algorithmproblem.jpg)

一. Divide anda Coonquer method :
  Recursive program Fib1 時間統計圖表及10秒中Fn最大的n值

  python code
  
    def fibonacci(n):
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

        print(fibonacci(5)))



二.Botton-up method:

  python code
    
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

        a = 0 
        b = 1 
        for c in range(0,n):
            a = b
            b = count
            count = a + b
            
    fibonacci(50)
    print(count)
    
三.Naive algorithm
  
  python code 
  
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

        count = math.pow(((1+(cmath.sqrt(5).real))/2), n )/(cmath.sqrt(5).real)

    fibonacci(5)
    print(count)
    
四.Recursive squaring method1
  
  python code 
  
    import cmath
    import math
    count = 0
    def fibonacci(n):
        global count
        if not isinstance(n, int):
            print ('Invalid Input')
            return None
        if n < 0:
            print ('Invalid Input')
            return None

        count = math.pow(((1+(cmath.sqrt(5).real))/2), n/2 )*math.pow(((1+(cmath.sqrt(5).real))/2), n/2 )

    fibonacci(2)
    print(count)
  
五.Recursive squaring method2

  python code
  
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


    fibonacci(100)
    print(count)
    
六.Negative Fibonacii numbers 

  python code 

    count = 0
    def fibonacci(n):
        global count
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
    
七.Lucas numbers

  python code

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
            
    fibonacci(50)
    print(count)

八.Tetranacci numbers

   python code
   
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
九.

