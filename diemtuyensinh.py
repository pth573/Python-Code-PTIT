# import math
#
# t = int(input())
# for i in range(0, t, 1):
#     name = list(input().split())
#     ten = []
#     for x in name:
#         ten.append(x[0].upper() + x[1:].lower())
#     ten = " ".join(ten)
#     diem = int(input())
#     dantoc = input().lower()
#     kv = int(input())
#     sum = diem
#     if(dantoc != "kinh"):
#         sum += 1.5
#     if(kv == 1):
#         sum += 1.5
#     elif kv == 2:
#         sum += 1
#     print(f"{'TS'}{(i + 1):02}: ", end="")
#     print(ten)
#     print(sum)
#     if(sum >= 20.5):
#         print("Do")
#     else:
#         print("Truot")
#
#     # print(ten)
#
#
# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3

# Hàm tính tổng điểm đã ưu tiên
def calculate_priority_score(diem, dantoc, kv):
    score = diem
    if dantoc.lower() != "kinh":
        score += 1.5
    if kv == 1:
        score += 1.5
    elif kv == 2:
        score += 1
    return score

# Đọc số lượng thí sinh
t = int(input())
candidates = []
for i in range(1, t + 1):
    name = list(input().split())
    ten = []
    for x in name:
        ten.append(x[0].upper() + x[1:].lower())
    name = " ".join(ten)
    diem = float(input())
    dantoc = input().strip()
    kv = int(input())
    score = calculate_priority_score(diem, dantoc, kv)
    status = "Do" if score >= 20.5 else "Truot"
    candidates.append((f"TS{i:02}", name, score, status))

# Sắp xếp danh sách thí sinh
sorted_candidates = sorted(candidates, key=lambda x: (-x[2], x[0]))

# In danh sách thí sinh đã sắp xếp
for i, (id, name, score, status) in enumerate(sorted_candidates, start=1):
    print(f"{id} {name} {score:.1f} {status}")
