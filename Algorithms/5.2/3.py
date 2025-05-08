def count_gcd_steps(a, b):
    count = 0
    while b:
        a, b = b, a % b
        count += 1
    return count

n = int(input())

best_a = 1
best_b = 1
max_steps = 0

a = 1
b = 1

while b <= n:
    steps = count_gcd_steps(a, b)
    if steps > max_steps:
        max_steps = steps
        best_a = a
        best_b = b

    a, b = b, a + b

print(best_a, best_b)
