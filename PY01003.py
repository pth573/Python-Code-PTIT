
def round_number(n):
    power = 10
    while n >= power:
        n = ((n + power // 2) // power) * power
        power *= 10
    return n

T = int(input())  

for _ in range(T):
    N = int(input())
    rounded_N = round_number(N)
    print(rounded_N)
