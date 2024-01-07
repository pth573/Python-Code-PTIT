import re

s = input()
li = re.findall("[4]", s)
li2 = re.findall("[7]", s)
if len(li) + len(li2) == 4 or len(li) + len(li2) == 7: 
    print("YES") 
else: 
    print("NO")