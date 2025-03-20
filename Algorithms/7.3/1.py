import random

def qsort(a):
    if len(a) <= 1: return a
    p = a[random.randint(0, len(a)-1)]
    l = [i for i in a if i < p]
    e = [i for i in a if i == p]
    g = [i for i in a if i > p]
    return qsort(l) + e + qsort(g)

n = int(input())
a = list(map(int, input().split()))
print(*qsort(a))
