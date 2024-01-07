


for _ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum = sum*10 + ord(x) - ord('0')
        sum %= 3
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")

# 2
# 12341
# 123456789123456789