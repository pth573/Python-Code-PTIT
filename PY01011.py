
import re

tmp = ['0', '2', '4', '6', '8']

def isTN(n):
    l, r = [0, len(n) - 1] 
    while l <= r:
        if n[l] != n[r]:
            return 0
        l+=1
        r-=1
    return 1

for _ in range(int(input())):
    n = input()
    arr = tmp.copy()
    while len(arr) > 0 and int(arr[0] + arr[0][::-1]) < int(n):
        if len(arr[0] + arr[0][::-1]) % 2 == 0 and int(arr[0] + arr[0][::-1]) > 0:
            print(int(arr[0] + arr[0][::-1]), end=" ")
        for i in range(len(tmp)):
            s = arr[0] + tmp[i]
            if not arr.count(str(int(s))):
                arr.append(s)
        arr.pop(0)
    print()
        
    