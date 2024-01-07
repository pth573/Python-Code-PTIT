
import math    
import re        

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1


for _ in range(int(input())):
    s = input()
    check = 1
    for j in range(0, len(s), 1):
        if isPrime(j):
            if isPrime(int(s[j])) == 0:
                check = 0
                break
        else:
            if isPrime(int(s[j])) == 1:
                check = 0
                break
    if check == 1:
        print("YES")
    else:
        print("NO")

# 2
# 14239567
# 2314514535353