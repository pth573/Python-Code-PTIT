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
    if isPrime(s[:3:]) == 1 and isPrime(s[-3::]) == 1:
        print("YES")
    else:
        print("NO")

            
# 3
# 12743
# 7337
# 12345678901234