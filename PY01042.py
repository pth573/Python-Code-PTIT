import re

for _ in range(int(input())):
    s = input()
    arr = re.findall("[^012]", s)
    if len(arr) > 0:
        print("NO")
    else:
        print("YES")
