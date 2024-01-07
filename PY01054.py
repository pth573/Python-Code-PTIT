for _ in range(int(input())):
    s = input()
    sum = 1
    for x in s:
        if x != '0':
            sum *= ord(x) - ord('0')
    print(sum)

# 2
# 123410
# 123456789123456789