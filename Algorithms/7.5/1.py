import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair_simple(points):
    n = len(points)
    if n < 2:
        return 0.0

    min_dist = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            min_dist = min(min_dist, dist)

    return min_dist

if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    result = closest_pair_simple(points)
    print(f"{result:.6f}")
