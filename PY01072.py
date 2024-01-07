
x = [0] * 1001 
ans = [] 

def solve(i, n, k):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            tmp = []
            for h in range(1, i + 1):
                tmp.append(arr[x[h] - 1])
            ans.append(tmp)
        elif i <= k:
            solve(i + 1, n, k)
            
n, k = list(map(int, input().split()))
arr = set(map(int, input().split()))
arr = sorted(arr)
# print(arr)
solve(1, len(arr), k)
for tmp in ans:
    for x in tmp:
        print(x, end = " ")
    print()