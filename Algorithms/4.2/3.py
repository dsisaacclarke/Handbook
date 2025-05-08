def solve():
  n = int(input())
  a = input()
  b = input()
  
  result = ""
  for i in range(n):
    result += a[i]
    result += b[i]
    
  print(result)
  
solve()
