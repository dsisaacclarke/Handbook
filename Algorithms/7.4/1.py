def count_inversions(arr):
    n = len(arr)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_inversions(arr))
