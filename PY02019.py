import math

n = int(input())
li = list(map(int, input().split()))
li.sort()
for i in range(n):
    for j in range(i + 1, n):
        if math.gcd(li[i], li[j]) == 1:
            print(li[i], li[j])