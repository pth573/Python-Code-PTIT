for _ in range(int(input())):
    s = input()
    tmp = s[0]
    check = 1
    for j in range(0, len(s), 2):
        if tmp != s[j]:
            check = 0
            break
        tmp = s[j]
    if len(s) % 2 == 1 and check == 1 and s[0] != s[1]:
        print("YES")
    else:
        print("NO")