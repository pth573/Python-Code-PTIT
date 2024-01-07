
import datetime

def format_time(a):
    return datetime.datetime.strptime(a, "%H:%M")

class rainQuanti:
    def __init__(self,id , name, quanti, total) -> None:
        self.id = id
        self.name = name
        self.quanti = quanti
        self.total = total

    def __str__(self) -> str:
        return f'T{self.id:02d}' + " " + self.name + " " + str(f'{(self.quanti / (self.total/ 3600)):.2f}')

dic = dict()
id = 1

for _ in range(int(input())):
    name = input()
    start = format_time(input())
    end = format_time(input())
    num = (end - start).seconds
    quanti = int(input())
    if name not in dic:
        dic[name] = rainQuanti(id, name, quanti, num)
        id += 1
    else:
        dic[name] = rainQuanti(dic[name].id, name, dic[name].quanti + quanti, dic[name].total + num)
for x in dic.values():
    print(x)
    

# 2
# DONG ANH 
# 07:30
# 08:00
# 60
# CAU GIAY
# 07:45
# 08:12
# 50


# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35