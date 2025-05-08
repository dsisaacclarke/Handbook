def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    max_product = float('-inf')
    max_product = max(max_product, a[-1] * a[-2] * a[-3] * a[-4])
    max_product = max(max_product, a[0] * a[1] * a[-1] * a[-2])
    max_product = max(max_product, a[0] * a[1] * a[2] * a[3])
    max_product = max(max_product, a[-1] * a[0] * a[1] * a[2])
        
    print(max_product)

solve()
