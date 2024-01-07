import math
n = int(input())
li = list(map(int, input().split()))
max = 0
arr = [0] * int(1e5)
for x in li:
    arr[x] = 1
    if x > max:
        max = x

check = 0
for i in range(1, max + 1):
    if arr[i] == 0:
        print(i)
        check = 1
        break
if check == 0:
    print(max + 1)
