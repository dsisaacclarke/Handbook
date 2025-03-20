def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if not arr:
        print(0)
        return

    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    threshold = n / 4
    count = 0
    for x in counts:
        if counts[x] > threshold:
            count += 1

    if count >= 3:
        print(1)
    else:
        print(0)

solve()
