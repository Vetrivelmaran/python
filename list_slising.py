class fibonacci:
    
    def __init__(self,n) -> None:
        self.n = n
    def fib(self):
        a =0
        b = 1
        for i in range(0,self.n):
            if i<=1:
                result = i
            else:
                result = a + b
                a = b
                b = result
            print(result)
ob = fibonacci(10)
ob.fib()


