def solve():
    n = int(input())
    all_nums = []
    for _ in range(n):
        m = int(input())
        nums = list(map(int, input().split()))
        all_nums.extend(nums)

    all_nums.sort()
    print(*all_nums)

solve()
