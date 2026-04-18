class Solution:
    def fib(self, n: int) -> int:
        
        cache = {0: 0, 1: 1}

        def fibonacci(n):
            if n < 0:
                return 0
            

            if n in cache:
                return cache[n]
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                return cache[n]
        return fibonacci(n)
            
            


