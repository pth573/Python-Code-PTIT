# import math

# a = [0] * 10000001
# check = [0] * 10000001
# maxx = 0

# def solve(n):
#     tmp = n
#     ans = 0
#     global a
#     for i in range(2, int(math.sqrt(n)) + 1, 1):
#         if(n % i == 0):
#             cnt = 0
#             while n % i == 0:
#                 cnt+=1
#                 n //= i
#             ans += cnt
#     if n > 1:
#         ans += 1
#     # a[tmp] = ans
#     return ans

# for i in range(1, 10000001, 1):
#     a[i]= solve(i)
#     print(a[i], end=" ")
#     # solve(i)
#     if a[i] > maxx:
#         check[i] = 1
        
#     maxx = max(a[i], maxx)




# for i in range(1, 10000001, 1):
#     print(check[i], end=" ")

# # for _ in range(int(input())):
# #     s = int(input())
# #     i = s
# #     while check[i] == 0:
# #         i+=1
# #     print(i)


def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
        if count > 4:
            return 0
    return 1

# def find_smallest_semiprime(X):
#     current_number = X
#     while True:
#         current_number += 1
#         count = count_divisors(current_number)
#         if count == 4:  # Số nguyên X có 4 ước số dương
#             return current_number
        

arr = [0] * 10000001

t = int(input())
for i in range(10000001):
    if count_divisors(i):
        arr[i] = 1
        print(i)

for _ in range(t):
    x = int(input())
    while tmp[x] != 1:
        x += 1
    print("hi", x)
    # result = find_smallest_semiprime(X)
    # print(result)
