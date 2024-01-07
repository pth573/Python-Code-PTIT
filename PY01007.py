for _ in range(int(input())):
    n, m, k = list(map(float, input().split()))
    cnt = 0
    while n < k:
        cnt += 1
        n += n * m / 100
    print(cnt)