import math    
import re        

def isPrime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1


for _ in range(int(input())):
    s = input()
    size = len(s)
    arr = re.findall("[2357]", s)
    if isPrime(size) == 1 and size - len(arr) < len(arr):
        print("YES")
    else:
        print("NO")

            
# 3
# 1234567
# 22334455667
# 23400300489898989