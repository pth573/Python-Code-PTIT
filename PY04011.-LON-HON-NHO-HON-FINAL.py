from collections import deque
ke = [[] for _ in range(100005)]
vao = [0] * 100005 
dinh = 0 
name_to_number = dict() 
for _ in range(int(input())):
    s1, s2, s3 = input().split()
    if s1 not in name_to_number:
        dinh += 1
        name_to_number[s1] = dinh
    if s3 not in name_to_number:
        dinh += 1
        name_to_number[s3] = dinh
    num_s1 = name_to_number[s1]
    num_s3 = name_to_number[s3]
    if s2 == ">":
        ke[num_s1].append(num_s3)
        vao[num_s3]+=1
    else:
        ke[num_s3].append(num_s1)
        vao[num_s1]+=1
q = deque()
for i in range(1, dinh + 1):
    if vao[i] == 0: q.append(i)
cnt = 0
while q:
    x = q.popleft()
    cnt += 1
    for i in ke[x]:
        vao[i] -= 1
        if vao[i] == 0: q.append(i)
if cnt == dinh: print("possible")
else: print("impossible")