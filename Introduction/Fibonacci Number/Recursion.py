
def f(n):
    if(n <= 1):
        return n
    
    last = f(n-1)
    slast = f(n-2)
        
    return last+slast

class Solution:
    def fib(self, n: int) -> int:
        return f(n)
      
