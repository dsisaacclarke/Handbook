def solve():
    n, k = map(int, input().split())
    x = sorted(map(int, input().split()))
    l, r = 0, x[-1] - x[0]

    def check(length):
        count, last = 1, x[0]
        for i in range(1, n):
            if x[i] - last > length:
                count += 1
                last = x[i]
        return count <= k

    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(l)

solve()
