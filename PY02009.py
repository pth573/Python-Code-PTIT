for _ in range(int(input())):
    a = [0] * 1001
    for i in range(int(input())):
        x = int(input())
        a[x] += 1
    arrnew = sorted(range(1001), key= lambda x : (-a[x], x))
    print(arrnew[0])
    
   
# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13