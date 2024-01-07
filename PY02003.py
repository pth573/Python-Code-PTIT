# import math
# # x = 1e18
# li = [1, 2, 3, 5]


# # print(math.log(x, 2))
# sum = 1
# k = 20

# while k >= 0:
#     for i in range(len(li)):
#         if not li.count(li[i] * 2):
#             li.append(li[i] * 2)
#         if not li.count(li[i] * 3):
#             li.append(li[i] * 3)
#         if not li.count(li[i] * 5):
#             li.append(li[i] * 5)
#     k -= 1
    
# li = sorted(li, key=lambda x : x)
# print(li)

# # for _ in range(int(input())):
# #     x = int(input())

from bisect import bisect_right, bisect_left

a = [1, 3, 3, 5, 7, 9, 11]

position = bisect_left(a, 12)

print(f"Vị trí để chèn số 6 là: {position}")





