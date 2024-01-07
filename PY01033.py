
def solve(a, b):
    if b == 0:
        return a
    return solve(b, a % b)

l, r = list(map(int, input().split()))
for i in range(l, r + 1, 1):
    for j in range(i + 1, r + 1, 1):
        if solve(i, j) == 1:
            for k in range(j + 1, r + 1, 1):
                if solve(i, k) == 1 and solve(j, k) == 1:
                    print(f'({i}, {j}, {k})')
        else:
            continue