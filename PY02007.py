
li = []
while(len(li) < 10):
    tmp = list(map(int, input().split()))
    li  = li + tmp
ans = set()
for x in li:
    ans.add(x % 42)
print(len(ans))
# 42 84 252 420 840
# 126 42 84 420 126

# 39 40 41 42 43 44 82
# 83 84 85




