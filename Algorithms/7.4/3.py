def count_transpositions(arr):
    def merge_sort(arr, temp_arr, left, right):
        inversions = 0
        if left < right:
            mid = (left + right) // 2
            inversions += merge_sort(arr, temp_arr, left, mid)
            inversions += merge_sort(arr, temp_arr, mid + 1, right)
            inversions += merge(arr, temp_arr, left, mid, right)
        return inversions

    def merge(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inversions = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inversions += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for l in range(left, right + 1):
            arr[l] = temp_arr[l]

        return inversions

    n = len(arr)
    temp_arr = [0] * n
    return merge_sort(arr, temp_arr, 0, n - 1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_transpositions(arr))
