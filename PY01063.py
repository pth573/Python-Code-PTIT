import math    
import re        



for _ in range(int(input())):
    s = input()
    n = input()
    li = re.finditer(n, s)
    print(len(li))
    cnt = 0
    for match in li:
        cnt+=1
    print(cnt)

    # C2:
    # li = [match for match in re.finditer(n, s)]
    # print(len(li))
    # for match in li:
    #     print(match.start())


# 2
# 1212121112211221121
# 121
# 2222222222322292
# 2222