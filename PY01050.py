

# ans = []
# def solve(n, cnt1, cnt2, cnt3, s):
#     global ans
#     if len(s) <= n and cnt1 >= 1 and cnt2 >= 1 and cnt3 >=1:
#         if cnt1 <= cnt2 and cnt2 <= cnt3:
#             ans.append(s)
#     if(cnt1 + cnt2 + cnt3 <= n):
#         solve(n, cnt1 + 1, cnt2, cnt3, s + 'A')
#         if cnt1 <= cnt2 + 1:
#             solve(n, cnt1, cnt2 + 1, cnt3, s + 'B')
#         if cnt2 <= cnt3 + 1:
#             solve(n, cnt1, cnt2, cnt3 + 1, s + 'C')

# n = int(input())
# solve(n, 0, 0, 0, "")
# ans.sort(key=lambda x : (len(x), x))
# for x in ans:
#     print(x)


def generate_permutations(string):
    n = len(string)
    if n == 0:
        return ['']

    perms = []
    for i in range(n):
        char = string[i]
        rest = string[:i] + string[i + 1:]
        rest_perms = generate_permutations(rest)
        for perm in rest_perms:
            perms.append(char + perm)

    return perms

def generate_strings(N):
    characters = "ABC"
    all_strings = set()

    for i in range(3, N + 1):
        permutations_list = generate_permutations(characters * i)
        for perm in permutations_list:
            if perm.count('A') <= perm.count('B') <= perm.count('C'):
                all_strings.add(perm)

    sorted_strings = sorted(list(all_strings), key=lambda x: (len(x), x))
    return sorted_strings

N = int(input())
strings = generate_strings(N)

for s in strings:
    print(s)
