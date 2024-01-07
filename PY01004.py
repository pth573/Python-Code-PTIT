import math
a = [0] * 1000000
def solve(a, b):
    if b == 0:
        return a
    else:
        return solve(b, a % b)

def isPrime():
    a[0] = a[1] = 1
    for i in range (2, int(math.sqrt(10001)), 1):
        if a[i] == 0:
            for j in range(i * i, 10001, i):
                a[j] = 1

isPrime()            
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n, 1):
        if solve(i, n) == 1:
            cnt+=1 
    # print(cnt)
    if a[cnt] == 0:
        print("YES")
    else:
        print("NO")

