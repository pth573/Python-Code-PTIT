import sys

def solve(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        solve(n // 2)
    else:
        cnt += 1
        solve(n * 3 + 1)

while(True):
    n = int(input())
    if n == 0:
        sys.exit()
    cnt = 1
    solve(n)
    print(cnt)
