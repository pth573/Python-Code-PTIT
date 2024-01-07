
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0    
    return n > 1

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if isPrime(solve(gcd(n, m))) == 1:
        print("YES")
    else:
        print("NO")
    