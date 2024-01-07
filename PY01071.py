import re

s = input()
s = s.lower()
arr = re.findall("[^a-zA-Z._]", s)
# print(arr)
if len(s) > 3 and s[-3::] == '.py' and len(arr) == 0:
    print("yes")
else:
    print("no")