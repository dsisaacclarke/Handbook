def solve():
  n = int(input())
  arr = list(map(int, input().split()))

  if not arr:
    print(0)
    return
  
  counts = {}
  for x in arr:
    counts[x] = counts.get(x, 0) + 1

  threshold = n / 2
  for x in counts:
    if counts[x] > threshold:
      print(1)
      return

  print(0)

solve()
