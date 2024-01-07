def solve(a, b):
    if b == 0:
        return a
    else:
        return solve(b, a % b)

for _ in range(int(input())):
    a = input()
    b = a[::-1]
    if solve(int(a), int(b)) == 1:
        print("YES")
    else:
        print("NO")
