import math

ans = ['1']

def solve(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt+=1
                n//=i
            x = str(i) + "^" + str(cnt)
            ans.append(x)
    if n > 1:
        x = str(n) + "^" + str(1)
        ans.append(x)

for _ in range(int(input())):
    tmp = input()
    tmp = int(tmp)
    solve(tmp)
    s = ' * '.join(ans)
    print(s)
    ans = ['1']