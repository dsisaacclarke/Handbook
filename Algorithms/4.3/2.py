def solve():
    n = int(input())

    if n <= 6:
        print("No")
        return

    print("Yes")
    result = [n] + list(range(1, n))
    print(*result)

solve()
