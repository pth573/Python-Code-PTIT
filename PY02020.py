n = int(input())
se = list(map(float, input().split()))
sum = 0
se = sorted(se, reverse=False)
x = se[0]
y = se[-1]
while se.count(x):
    se.remove(x)
while se.count(y):
    se.remove(y)
for x in se:
    sum += x
tmp = "{:.2f}".format(sum/len(se))
print(tmp)
