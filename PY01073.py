
ans = []
x = [0] * 101
visited = [''] * 101

def solve(i, s):
    global x
    global ans
    for j in s:
        if not visited[j]:
            x[i] = j
            visited[j] = 1
            if i == len(s):
                tmp = []
                for h in range(1, i + 1, 1):
                    tmp.append(x[h])
                ans.append(tmp)
            elif i <= len(s):
                solve(i + 1, s)
            visited[j] = 0

s = input()
solve(1, s)
for tmp in ans:
    for x in tmp:
        print(x, end="")
    print()
print(ans)

# ans = []

# def generate_permutations(s, current='', index=0):
#     if index == len(s):
#         # print(current)
#         ans.append(current)
#         return
#     for i in range(len(current) + 1):
#         new_permutation = current[:i] + s[index] + current[i:]
#         generate_permutations(s, new_permutation, index + 1)

# s = input()
# # s = set(s)
# s = list(set(s))
# # print(s)
# generate_permutations(s)
# ans.sort()
# for x in ans:
#     print(x)

S = "HELLO"
S = S[-1:]
print(S)

