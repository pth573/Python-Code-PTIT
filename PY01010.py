for _ in range(int(input())):
    s = input()
    # print(s[0:2])
    # print(s[-2:])
    # print(s[len(s) - 2: len(s)])
    if s[0:2] == s[len(s) - 2: len(s)]:
        print("YES")
    else:
        print("NO")