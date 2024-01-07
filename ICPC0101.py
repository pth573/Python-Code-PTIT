n = int(input())
arr = list(map(int, input().split()))
tmp = []
for x in arr:
    if len(tmp) == 0:
        tmp.append(x)
    else:
        if (tmp[-1] + x) % 2 == 0:
            tmp.pop()
        else:
            tmp.append(x)
print(len(tmp))