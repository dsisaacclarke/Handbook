def solve():
  n = int(input())
  a = list(map(int, input().split()))
  m = int(input())
  b = list(map(int, input().split()))

  max_degree = max(n, m)
  
  result = []
  for i in range(max_degree + 1):
    coeff_a = 0
    coeff_b = 0
    
    if n - i >= 0:
      coeff_a = a[n - i]
    if m - i >= 0:
      coeff_b = b[m - i]
      
    result.append(coeff_a + coeff_b)
    
  while len(result) > 1 and result[-1] == 0:
      result.pop()

  print(len(result) - 1)
  print(*result[::-1])

solve()
