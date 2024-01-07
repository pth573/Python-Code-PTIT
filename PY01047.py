import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return 0
    return n > 1

for _ in range(int(input())):
    s = input()
    s = s[-4::]
    if isPrime(int(s)) == 1:
        print("YES")
    else:
        print("NO")

# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999