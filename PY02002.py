fibo = [0] * 95

def solve():
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

solve()
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        print(fibo[i], end=" ")
    print()

    
