

arr = []
n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n - 1):
    if(arr[i] != arr[i + 1]):
        cnt += 1
print(cnt)