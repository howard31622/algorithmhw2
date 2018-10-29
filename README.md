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

時間統計圖：

![image](https://github.com/howard31622/algorithmhw2/blob/master/fib1.png)

十秒內最大的n值： 7049155


二.Botton-up method:Fib2求時間統計圖表及10秒中Fn最大的n值

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
            
    fibonacci(5)
    print(count)
    
時間統計圖：

![image](https://github.com/howard31622/algorithmhw2/blob/master/fib2.png)    
    
十秒內最大的n值：
	在64位元中最大值為fib2(305) ，在fib(306)時因為超過範圍了，故不計算。
	
  而 n = 305 時算出的fib2(305) = 6452389184720949856740872794933738025334109298792472139250504213
  
  而 n = 306 時算出的fib2(306) = 10440185009520720572083697583620800653786381708749108822250120621
    
    
三.Naive algorithm : Fib3求時間統計圖表及10秒中Fn最大的n值，在這個做法中有哪些Fn會算錯，如果要提高正確率的方法
  
  python code 
  
    count = 0
    def fibonacci(n):
        global count
        if not isinstance(n, int):
            print ('Invalid Input')
            return None
        if n < 0:
            print ('Invalid Input')
            return None
        count = (( (1 + (5 ** 0.5))/2) ** n)/(5 ** 0.5)

    fibonacci(5)
    print(count)
    
時間統計圖：

![image](https://github.com/howard31622/algorithmhw2/blob/master/fib3.png)

十秒內最大的n值：（因為數字超過範圍，因此只能顯示64位元中最大數字）
	這個算出來的值會超出範圍，因此還是使用n = 305 求出最大數 2.4645933599212044e+63

    
四.Recursive squaring method1 : 利用Fn = (φ^(n/2)) * (φ^(n/2))為Fib4求時間統計圖表及10秒中Fn最大的n值，而這個做法會有哪些會算錯
  
  python code 
  
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
 
 時間統計圖：
 
![image](https://github.com/howard31622/algorithmhw2/blob/master/fib3.png)
 
 十秒內最大的n值：（因為數字超過範圍，因此只能顯示64位元中最大數字）
	這個算出來的值會超出範圍，因此還是使用n =305求出最大數，這兩個的時間複雜度不一樣，但所算出的時間卻看似一樣，可能是因為，題目所設定的範圍不夠

 
五.Recursive squaring method2 : 利用Fn =[[1 1],[1 0]]為Fib5求時間統計圖表及10秒中Fn最大的n值


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
   	
    fibonacci(5)
    print (count[0][0])
    
時間統計圖：

![image](https://github.com/howard31622/algorithmhw2/blob/master/fib5.png)

十秒內最大的n值：	
根據實驗結果，算出當n = 9000000在約十秒的時候算出答案 => 8434530251446700417

六.Negative Fibonacii numbers : 利用 Fn-2  = Fn – Fn-1 做出Fib6 


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
    
七.Lucas numbers : 利用定義寫出Fib7

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


八.Tetranacci numbers : 利用這個method延伸出提供前Ｋ個數字相加求第n個Fib8  Fn,k ，並求時間跟空間複雜度

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
      
從上面的程式碼中可以看出，空間複雜度是以O(k) 因為我使用陣列去處理，時間複雜度為O(n+1)
      
九.
參考資料：http://www.montefiore.ulg.ac.be/~piater/courses/INFO0902/notes/basic-algos/foil15.xhtml
這次作業對我來說碰到最大的困難應該都是在求時間成長統計表，因為求數據很花時間，也不太想用python直接畫圖
