def solve(a, b):
    if b == 0:
        return a
    else:
        return solve(b, a % b)
    
n, k = list(map(int, input().split()))
# n = int(input())
# k = int(input())
cnt = 0
for i in range(10 ** (k - 1), 10 ** k - 1, 1):
    if solve(int(n), int(i)) == 1:
        print(i, end=" ")
        cnt+=1
        if cnt % 10 == 0:
            print()