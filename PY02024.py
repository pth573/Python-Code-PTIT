def solve(n):
    sum = 1
    while(n > 0):
        sum *= n % 10
        n //= 10
    return sum

for _ in range(int(input())):
    n = int(input())
    ans = []
    li = list(map(int, input().split()))
    li = sorted(li, key= lambda x : (solve(x), x))
    for x in li:
        print(x, end = " ")
# 1
# 8
# 143 43 22 99 7 9 1111 10000000