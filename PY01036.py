for _ in range(int(input())):
    sum = 0.0
    n = int(input())
    for i in range(1, n + 1, 1):
        if n % 2 == 0:
            if i % 2 == 0:
                sum += 1/i
        else:
            if i % 2 != 0:
                sum += 1/i
    print(f'{sum:.6f}')