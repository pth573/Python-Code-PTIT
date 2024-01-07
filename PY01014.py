a, k, n = list(map(int, input().split()))
check = 0
b = n - a + 1
for i in range(1, b, 1):
    if (i + a) % k == 0:
        print(i, end=" ")
        check = 1
if check == 0:
    print("-1")

