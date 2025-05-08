def solve():
    n = int(input())

    if n <= 1:
        print(n)
        return

    a = 0
    b = 1

    for _ in range(2, n + 1):
        c = (a + b) % 10
        a = b
        b = c

    print(b)

solve()
