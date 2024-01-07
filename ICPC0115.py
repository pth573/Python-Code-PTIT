import math

for _ in range(int(input())):
    n = input()
    sum = 0
    for x in n:
        sum += math.factorial(int(x))
    print("Yes") if int(n) == sum else print("No")
