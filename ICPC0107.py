

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    max1 = int(str1.replace("5", "6"))
    max2 = int(str2.replace("5", "6"))
    # print(max1, " ", max2)
    min1 = int(str1.replace("6", "5"))
    min2 = int(str2.replace("6", "5"))
    # print(min1, " ", min2)
    print(f"{min1 + min2} {max1 + max2}")
    # print(min1 + min2," ", max1 + max2)
