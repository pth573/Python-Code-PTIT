
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1



for _ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum += ord(x) - ord('0')
    if isPrime(sum):
        print("YES")
    else:
        print("NO")
# 2
# 12341
# 22222222222222222222