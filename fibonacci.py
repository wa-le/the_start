# Fibonacci sequence (next number is the addition of the two previous numbers)

def fibo(n):
    x = 0
    y = 1
    print(x)
    print(y)
    
    for _ in range(2, n):
        z = x + y
        x = y
        y = z
        
        print(z)
        
fibo_reach = int(input("Enter number for fibo to reach: "))
fibo(fibo_reach)