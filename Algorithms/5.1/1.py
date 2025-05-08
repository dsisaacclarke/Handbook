def solve():
    n = int(input())
    
    if n <= 1:
        print(n)
        return
    
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
        
    print(fib[n])

solve()
