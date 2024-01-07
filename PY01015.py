def solve(n):
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            return 0
    return 1

for _ in range(int(input())):
    s = input()
    print("YES") if solve(s) == 1 else print("NO")