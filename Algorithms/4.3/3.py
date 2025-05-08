def solve():
  n = int(input())
  a = list(map(int, input().split()))
  
  a.sort()
  
  max_product = max(a[-1] * a[-2] * a[-3], a[0] * a[1] * a[-1])
  
  print(max_product)
  
solve()
