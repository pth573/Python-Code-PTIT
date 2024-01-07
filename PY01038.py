

for _ in range(int(input())):
    n = input()
    m = n[::-1]
    cnt = 0
    if int(n) % 7 == 0:
        print(n)
        continue
    while (int(n) + int(m)) % 7 != 0:
        n = str(int(n) + int(m))
        m = n[::-1]
        cnt+=1
        if cnt > 1000:
            break
    if (int(n) + int(m)) % 7 != 0:
        print("-1")
    else:
        print(int(n) + int(m))