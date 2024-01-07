

# for _ in range(int(input())):
#     n = input()
#     m = n[::-1]
#     cnt = 0
#     while (int(n) + int(m)) % 7 != 0:
#         n = str(int(n) + int(m))
#         m = n[::-1]
#         cnt+=1
#         if cnt > 1000:
#             break
#         # print(n, " ", m)
#     if (int(n) + int(m)) % 7 != 0:
#         print("-1")
#     else:
#         print(int(n) + int(m))

def solve(n):
    x = n[0]
    y = n[1]
    for i in range(len(n)):
        if i % 2 == 0:
            if x != n[i]:
                return 0
        else:
            if y != n[i]:
                return 0
    return 1


for _ in range(int(input())):
    n = input()
    if len(n) > 1:
        if solve(n):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
        continue

