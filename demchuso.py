# # Hàm tính tần số của chữ số từ A đến B
# def count_digit_frequency(A, B):
#     # Khởi tạo mảng tần số
#     frequency = [0] * 10
#
#     # Duyệt qua các số từ A đến B
#     for num in range(A, B + 1):
#         digits = list(str(num))  # Chuyển số thành chuỗi và tách thành các chữ số
#         for digit in digits:
#             frequency[int(digit)] += 1
#
#     return frequency
#
# # Đọc số lượng bộ test
# T = int(input())
#
# # Xử lý từng bộ test
# for _ in range(T):
#     A, B = map(int, input().split())
#     frequency = count_digit_frequency(A, B)
#
#     # In ra mảng tần số
#     print(*frequency)
#
# # Kết thúc

#
# def count_digit_frequency(A, B):
#     frequency = [0] * 10
#
#     for num in range(A, B + 1):
#         while num > 0:
#             digit = num % 10
#             frequency[digit] += 1
#             num //= 10
#
#     return frequency
#
# T = int(input())
#
# for _ in range(T):
#     A, B = map(int, input().split())
#     frequency = count_digit_frequency(A, B)
#     print(*frequency)


def count_digit_frequency(A, B):
    frequency = [0] * 10

    # Chuyển A và B thành chuỗi để dễ dàng duyệt qua từng chữ số
    A_str = str(A)
    B_str = str(B)

    # Tính độ dài của chuỗi B_str
    len_B_str = len(B_str)

    for digit in range(10):
        for len_A in range(1, len_B_str):
            # Duyệt qua từng vị trí trong chuỗi B_str
            for i in range(len_B_str):
                # Xét các trường hợp đặc biệt
                if len_A == 1 and i == 0 and digit == 0:
                    continue
                if i == 0 and digit == 0:
                    continue

                if len_A == len_B_str:
                    if int(B_str[i]) > digit:
                        frequency[digit] += int(B_str[:i]) + 1
                    elif int(B_str[i]) == digit:
                        frequency[digit] += int(B_str[:i])
                    else:
                        frequency[digit] += int(B_str[:i])
                else:
                    if int(B_str[i]) > digit:
                        frequency[digit] += int(B_str[:i])
                    elif int(B_str[i]) == digit:
                        frequency[digit] += int(B_str[:i])
                    else:
                        frequency[digit] += int(B_str[:i]) - 1

            if len_A == len_B_str:
                if A <= int(B_str[:len_A]):
                    if int(B_str[len_A - 1]) >= digit:
                        frequency[digit] -= int(B_str[:len_A])
                    else:
                        frequency[digit] -= int(B_str[:len_A]) - 1
                elif int(B_str[len_A - 1]) >= digit:
                    frequency[digit] -= int(B_str[:len_A])
                else:
                    frequency[digit] -= int(B_str[:len_A]) - 1

            if len_A < len_B_str:
                if A <= int(B_str[:len_A]):
                    frequency[digit] -= int(B_str[:len_A])
                else:
                    frequency[digit] -= int(B_str[:len_A]) - 1

    return frequency

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    frequency = count_digit_frequency(A, B)
    print(*frequency)
