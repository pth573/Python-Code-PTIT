n = int(input())
li = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if li[i] > li[j]:
            cnt += 1
print(cnt)