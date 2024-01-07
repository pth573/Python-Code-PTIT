arr = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
while 1:
    li = list(input().split())
    if(len(li) == 1):
        break
    elif(len(li) == 2):
        k = li[0]
        s = li[1]
        k = int(k)
        if k == 0:
            break
        for i in range(len(s) - 1, -1, -1):
            tmp = ord(s[i]) - ord('A')
            if s[i] == '_':
                tmp = 26
            elif s[i] == '.':
                tmp = 27
            print(arr[(tmp + k) % 28], end="")
        print()