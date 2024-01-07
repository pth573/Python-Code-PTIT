for _ in range(int(input())):
    s = input()
    i = 0
    # tmp = s[0]
    while i < len(s):
        tmp = s[i]
        cnt = 0
        while i < len(s) and tmp == s[i]:
            cnt+=1
            i+=1 
        print(f'{cnt}{tmp}', end="")
        if i < len(s):
            tmp=s[i]
    print()

