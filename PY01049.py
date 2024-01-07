import math
import re

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1

for _ in range(int(input())):
    s = input()
    tmp = re.findall("[2357]", s)
    tmp2 = re.findall("[^2357]", s)
    if isPrime(len(s)) == 1 and len(tmp) > len(tmp2):
        print("YES")
    else:
        print("NO")


# 3
# 1234567
# 22334455667
# 23400300489898989