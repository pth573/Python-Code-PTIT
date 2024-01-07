for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = [0] * int(1e6 + 1)

    for x in li:
        cnt[x] += 1
    li = sorted(li, key=lambda x : (-cnt[x], x))
    check = -1
    for x in li:
        if cnt[x] > n / 2:
            print(x)
            check = 1
            break
    if check == -1:
        print("NO")
