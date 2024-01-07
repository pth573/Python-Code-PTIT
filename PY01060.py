import math    

for _ in range(int(input())):
    s = input()
    sum = 0
    mul = 1
    check = 1
    for j in range(0, len(s), 1):
        if j % 2 != 0:
            sum += int(s[j])
        else:
            if s[j] != '0':
                check = 0
                mul *= int(s[j])
    if check != 0:
        print("0", end=" ")
    else:
        print(mul, end = " ")
    print(sum)

            
# 3
# 12345678
# 20000
# 22334455667788