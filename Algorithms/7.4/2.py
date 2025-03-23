def count_semi_inversions_fenwick(arr):
    def update(bit, i, v):
        while i < len(bit):
            bit[i] += v
            i += i & -i

    def query(bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    sorted_arr = sorted(list(set(arr)))
    rank = {val: i + 1 for i, val in enumerate(sorted_arr)}

    n = len(sorted_arr)
    bit = [0] * (n + 1)

    semi_inversions = 0
    for i in range(len(arr) - 1, -1, -1):
        semi_inversions += query(bit, rank[arr[i]])
        update(bit, rank[arr[i]], 1)

    return semi_inversions

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_semi_inversions_fenwick(arr))
