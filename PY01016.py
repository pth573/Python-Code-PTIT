import re
for _ in range(int(input())):
    s = input()
    num = re.findall("[0-9]+", s)
    alpha = re.findall("[A-Z]", s)
    for i in range(0, len(alpha)):
        print(alpha[i] * int(num[i]), end="")
    print()