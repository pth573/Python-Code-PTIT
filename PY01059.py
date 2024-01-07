import math    
import re        

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1


for _ in range(int(input())):
    s = input()
    sum = 0
    mul = 1
    check = 1
    for j in range(0, len(s), 1):
        if j % 2 == 0:
            sum += int(s[j])
        else:
            if s[j] != '0':
                check = 0
                mul *= int(s[j])
            # else:
            #     mul *= int(s[j])
    print(sum, end=" ")
    if check != 0:
        print("0")
    else:
        print(mul)

            
# 3
# 12345678
# 20000
# 22334455667788