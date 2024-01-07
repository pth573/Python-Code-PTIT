
import re



arr = []

class player:
    def __init__(self, id, name, timeIn, timeOut) -> None:
        self.id = id
        self.name = name
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.totalTime = 0
        self.s = self.solve()
    def solve(self):
        a, b = map(int, re.findall("\d+", self.timeIn))
        c, d = map(int, re.findall("\d+", self.timeOut))
        x = c * 60 + d - (a * 60 + b)
        self.totalTime = x
        return f'{x // 60} gio {x % 60} phut'
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + self.s


for _ in range(int(input())):
    arr.append(player(input(), input(), input(), input())) 
arr = sorted(arr, key = lambda x : (-x.totalTime))

for x in arr:
    print(x)


# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00