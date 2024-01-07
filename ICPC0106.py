import math

def solve(n, k):
    if n == 0:
        return
    solve(n // k, k)
    if n % k < 10:
        print(n % k, end = "")
    else:
        print(chr(ord('A') + n % k - 10), end = "")

for _ in range(int(input())):
    k = int(input())
    s = input()
    s = int(s, 2)
    if s == 0: 
        print("0")
    else:
        solve(s, k)
        print()

# 2
# 8
# 10010100010010101
# 2
# 10010100010010101