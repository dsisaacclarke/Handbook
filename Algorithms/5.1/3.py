n, m = (int(i) for i in input().split())
n1 = 0
n2 = 1
if n == 1:
    print(1)
else:
    ost = [0]

    l = -1

    for i in range(n):
        n1, n2 = n2, n1 + n2
        ost.append(n1 % m)

        if i > m and ost[:m] == ost[-m::1]:
            l = i
            break
    if l != -1:
        ost = ost[:-m]

    print(ost[n % len(ost)])
