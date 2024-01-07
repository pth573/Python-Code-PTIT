import math



def solve(n):
    ans = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        while n % i == 0:
            ans += i
            n //= i
    if n > 1:
        ans += n
    return ans

sum = 0
for _ in range(int(input())):
    n = int(input())
    sum += solve(n)
print(sum)