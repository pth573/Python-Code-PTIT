
def sum(n):
    n = int(n)
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans % 10 == 0

def solve(n):
    for i in range(0, len(n) - 1, 1):
        if abs((ord(n[i])) - ord(n[i + 1])) != 2:
            return 0
    return 1


for _ in range(int(input())):
    s = input()
    if sum(s) == 1 and solve(s):
        print("YES")    
    else:
        print("NO")
