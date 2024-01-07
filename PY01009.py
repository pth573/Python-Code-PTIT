import re

s = input()
li = re.findall("[a-z]", s)
li2 = re.findall("[A-Z]", s)
if len(li) < len(li2):
    s = s.upper()
else:
    s = s.lower()
print(s)