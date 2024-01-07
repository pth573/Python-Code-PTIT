# # import re

# # # s = "XIn chao chao Rat ca moin8guoi tui 2012"
# # # li = re.findall("\w+", s)
# # # for x in li:
# # #     print(x)


# # import datetime

# # li = ["5/7/2003", "9/9/2002", "8/8/2002"]
# # li = [datetime.datetime.strptime(x, "%d/%m/%Y") for x in li]

# # li = sorted(li, key=lambda x : (x.timestamp()))

# # for x in li:
# #     print(x)
# # # x = x.strftime("%d/%m/%Y")
# # # print(x)


# # # Danh sách các chuỗi
# # my_list = ["apple", "Banana", "Orange", "grape", "Cherry", "Apple"]

# # # Sắp xếp theo chuỗi viết thường
# # sorted_list = sorted(my_list, key=lambda x: (x.lower(), x[0]), reverse=[True, False])

# # # In kết quả
# # print(sorted_list)


# # my_list = ["apple", "Banana", "Orange", "grape", "Cherry", "Apple"]
# # sorted_list = sorted(my_list, key=lambda x: (x.lower(), x))
# # print(sorted_list)






# # 

# # sorted_list = sorted(my_list, key=lambda x: (x[0].lower()))
# # print(sorted_list)


# import functools


# my_list = ["apple", "Banana", "orange", "grape", "Cherry", "Appl"]


# def cmp_function(x, y):
#     return x.lower() - y.lower()
#     # if x.lower() < y.lower():
#     #     return -1
#     # elif x.lower() > y.lower():
#     #     return 1
#     # else:
#     #     if x[0] < y[0]:
#     #         return -1
#     #     elif x[0] > y[0]:
#     #         return 1
#     #     else:
#     #         return 0

# sorted_list = sorted(my_list, key=functools.cmp_to_key(cmp_function))

# print(sorted_list)



def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            shifted_index = (char_index + shift) % 26
            shifted_char = chr(shifted_index + ord('a'))
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char
    return result

# Input
num_tests = int(input())
for _ in range(num_tests):
    test_input = input().split()
    input_string, shift_amount = test_input[0], int(test_input[1])
    
    # Output
    print(caesar_cipher(input_string, shift_amount))
