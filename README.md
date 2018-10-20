# algorithmhw2

This project is for algorithm homework2

homework introduction
![image](https://github.com/howard31622/algorithmhw2/blob/master/algorithmproblem.jpg)

一. Divide anda Coonquer method :
  Recursive program Fib1 時間統計圖表及10秒中Fn最大的n值

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

    fibonacci(50)
    print(count)



二.Botton-up method:
