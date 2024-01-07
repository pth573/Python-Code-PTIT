
class sv:
    def __init__(self, name, num, submit) -> None:
        self.name = name
        self.num = num
        self.submit = submit
    def __str__(self) -> str:
        return self.name + " " + str(self.num) + " " + str(self.submit)

li = []
for _ in range(int(input())):
    name = input()
    num, submit = list(map(int, input().split()))
    li.append(sv(name, num, submit))
li = sorted(li, key= lambda x : (-x.num, x.submit, x.name))
for x in li:
    print(x)

# 2
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 168 600
# Tran Thi Ngoc 168 600
# Tran Thi Ngoc 168 600