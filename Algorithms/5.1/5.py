def solve():
    m, n = map(int, input().split())

    def fib_last_digit(k):
        k = k % 60
        if k <= 1:
            return k
        a = 0
        b = 1
        for _ in range(2, k + 1):
            a, b = b, (a + b) % 10
        return b

    Fn2 = fib_last_digit(n + 2)
    Fm1 = fib_last_digit(m + 1)

    result = (Fn2 - Fm1) % 10

    if result < 0:
        result += 10

    print(result)

solve()
