
def solve(n):
    if len(n) < 3:
        return 0
    i = 0
    while(i < len(n) - 1 and n[i] < n[i + 1]):
        i+=1
    j = len(n) - 2
    while(j >= 0 and n[j] > n[j + 1]):
        j-=1
    j+=1
    return i == j 

for _ in range(int(input())):
    n = input()
    print("YES") if solve(n) else print("NO")