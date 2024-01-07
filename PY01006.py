import re
for _ in range(int(input())):
    s = input()
    li = re.findall("[^47]", s)
    if len(li) == 0:
        print("YES") 
    else: 
        print("NO")