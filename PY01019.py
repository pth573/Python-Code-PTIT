
import math
for _ in range(int(input())):
    s = input()
    res = s[::-1]
    check = 1
    for i in range(1, len(s), 1):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(res[i]) - ord(res[i - 1])):
            check = 0 
            break
    print("YES") if check == 1 else print("NO")