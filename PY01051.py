

for _ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum += ord(x) - ord('0')
    sum = str(sum)
    if sum == sum[::-1] and len(sum) > 1:
        print("YES")
    else:
        print("NO")


# 2
# 12341
# 22222222222222222222