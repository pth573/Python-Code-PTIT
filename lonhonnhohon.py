# def is_possible(N):
#     graph = {}  # Danh sách kề để lưu trữ mối quan hệ giữa các thành viên
#     in_degree = {}  # Số bậc vào của mỗi thành viên
#
#     # Khởi tạo đồ thị và bậc vào
#     for _ in range(N):
#         a, op, b = input().split()
#         if op == '>':
#             if b not in graph:
#                 graph[b] = []
#             graph[b].append(a)
#             in_degree[a] = in_degree.get(a, 0) + 1
#         else:
#             if a not in graph:
#                 graph[a] = []
#             graph[a].append(b)
#             in_degree[b] = in_degree.get(b, 0) + 1
#
#     # Sử dụng thuật toán topology để kiểm tra chu trình
#     queue = [name for name in graph if name not in in_degree]
#     while queue:
#         node = queue.pop()
#         for neighbor in graph.get(node, []):
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     # Nếu có chu trình trong đồ thị, thì không thể có phép so sánh nào đúng
#     if len(in_degree) != len(graph):
#         return "impossible"
#     else:
#         return "possible"
#
# # Đọc dữ liệu vào
# N = int(input())
# # comparisons = [input() for _ in range(N)]
#
# # Gọi hàm kiểm tra và in kết quả
# result = is_possible(N)
# print(result)
#
#
# # 3
# # An > Binh
# # Binh > Cong
# # An < Cong

def is_possible(N, comparisons):
    # Khởi tạo danh sách các thành viên và biểu đồ có hướng
    members = set()
    graph = {}

    # Xây dựng biểu đồ và ghi nhớ số bậc vào của mỗi thành viên
    in_degree = {}
    for i in range(N):
        a, op, b = comparisons[i].split()
        members.add(a)
        members.add(b)
        if op == ">":
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
            in_degree[a] = in_degree.get(a, 0) + 1
        else:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            in_degree[b] = in_degree.get(b, 0) + 1

    # Sử dụng thuật toán topology để kiểm tra xem có chu trình hay không
    queue = [member for member in members if member not in in_degree]
    while queue:
        member = queue.pop(0)
        for neighbor in graph.get(member, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Kiểm tra xem có chu trình (cycle) hay không
    if len(queue) == len(members):
        return "possible"
    else:
        return "impossible"


# Đọc dữ liệu vào
N = int(input())
comparisons = [input() for _ in range(N)]

# Gọi hàm kiểm tra và in kết quả
result = is_possible(N, comparisons)
print(result)


# 3
# An > Binh
# Binh > Cong
# An > Cong