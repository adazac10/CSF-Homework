def fib(n):
        if n == 0 or n == 1:
            return 1
        return fib(n-1) + fib(n-2)
            
# def testfib(n):
#       for i in range(n+1):
#              print ('fib of, i, '-', fib(i)')
                

print fib(6) 




series = raw_input("Enter string ")
n =6

def lab3fib():
    if series == 'fibonacci':
        return fib(n)
    elif series == 'sum':
        return sum(range(0, 3 * n + 1, 3))
    else:
        return 0
        
        
print lab3fib() + 1

                
              