def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

n = int(input())
k = list(map(int, input().split()))

m = int(input())
q = list(map(int, input().split()))

for query in q:
    index = binary_search(k, query)
    print(index)
