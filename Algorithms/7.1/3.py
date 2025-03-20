def count_occurrences(arr, target):
  first = find_first(arr, target)
  if first == -1:
    return 0
  return find_last(arr, target) - first + 1

def find_first(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return low if low < len(arr) and arr[low] == target else -1


def find_last(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] > target:
      high = mid - 1
    else:
      low = mid + 1
  return high


n = int(input())
k = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

for query in q:
  print(count_occurrences(k, query))
