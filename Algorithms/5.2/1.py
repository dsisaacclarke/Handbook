def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    a, b = map(int, input().split())
    print(gcd(a, b))

solve()
