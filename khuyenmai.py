[a, b, c] = list(map(int, input().split()))
print(-1) if (a + b) // b * b >= c + 1 else print(' '.join([str(x - a) for x in range((a + b) // b * b, c + 1, b)]))