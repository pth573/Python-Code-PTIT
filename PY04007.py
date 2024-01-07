
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[0] * m for i in range(n)]
    b = [[0] * n for i in range(m)]
    c = [[0] * n for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end = " ")
        print()

