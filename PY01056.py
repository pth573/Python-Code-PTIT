
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1

def solve(n):
    for i in range(0, len(n), 1):
        if i % 2 == 0:
            if (ord(n[i]) - ord('0')) % 2 != 0:
                return 0
        else:
            if (ord(n[i]) - ord('0')) % 2 == 0:
                return 0
    return 1
                

for _ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum += ord(x) - ord('0')
    if isPrime(sum) == 1 and solve(s) == 1:
        print("YES")
    else:
        print("NO")
# 2
# 2345678521
# 1212121212121212121212121