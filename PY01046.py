def solve(n, a, b, c):
    if n == 1:
        print(f'{a} -> {c}')
        return
    solve(n - 1, a, c, b)
    print(f'{a} -> {c}')
    solve(n - 1, b, a, c)

s = int(input())
solve(s, 'A', 'B', 'C')

