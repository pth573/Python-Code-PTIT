s = input()
while(len(s) % 3 != 0):
    s = '0' + s
# print(s)
substr = [s[i : i + 3] for i in range(0, len(s), 3)]
# print(substr)

for x in substr:
    print(int(x, 2), end="")