import re

s = ''
while True:
    try:
        s += input() + " "
    except EOFError:
        break
s=s.lower()
s = re.split('[.?!]', s)
ans = ""
for x in s:
    x = x.strip()
    li = x.split()
    if len(li) > 0: 
        li[0] = li[0].title()
        ans = ' '.join(li)
        print(ans)