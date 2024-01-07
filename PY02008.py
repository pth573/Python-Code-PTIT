import math

prime = [0] * 10001
li = []
def snt():
    prime[0] = 1
    prime[1] = 1
    for i in range(2, int(math.sqrt(1e4)) + 1, 1):
        if not prime[i]:
            for j in range(int(i * i), int(1e4) + 1, i):
                prime[j] = 1
    for i in range(int(1e4) + 1):
        if not prime[i]:
            li.append(i)

snt()
n, x = map(int, input().split())
print(x, end = " ")
for i in range(n):
    x += li[i]
    print(x, end = " ")
