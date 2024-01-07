import math

def snt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n > 1

n, m = map(int, input().split())
li = []
for i in range(n):
    tmp = list(map(int, input().split()))
    li.append(tmp)
for x in li:
    for k in x:
        if snt(k):
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()