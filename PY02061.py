

# dung / de ngat dong nhieu dau cong


def mul(a, b, c, n, m):
    global sum
    k = m - 2
    h = n - 2
    for i in range(h):
        for j in range(k):
            c[i][j] = a[i][j] * b[0][0] + a[i][j + 1] * b[0][1] + a[i][j + 2] * b[0][2] \
                + a[i + 1][j] * b[1][0] + a[i + 1][j + 1] * b[1][1] + a[i + 1][j + 2] * b[1][2] \
                + a[i + 2][j] * b[2][0] + a[i + 2][j + 1] * b[2][1]+ a[i + 2][j + 2] * b[2][2]
            sum += c[i][j]


for _ in range(int(input())):
    
    n, m = list(map(int, input().split()))
    sum = 0
    a = [[0] * m] * n
    for i in range(n):
        a[i] = list(map(int,input().split()))
    b = [[0] * 3] * 3
    for i in range(3):
        b[i] = list(map(int,input().split()))
    c = [[0] * (m - 2)] * (n - 2)
    mul(a, b, c, n, m)
    print(sum)

# 2
# 4 4
# 2 1 0 0 
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1