n, m = map(int, input().split())
a = [int(x) for x in input().split()]


def loop(i, exp):
    if i == n:
        res.append(exp)
        return
    num = a[i]
    loop(i + 1, exp + f' + {num}')
    loop(i + 1, exp + f' - {num}')
    loop(i + 1, exp + f' * {num}')


def check(s):
    b = s.split()
    while '*' in b:
        for i in range(len(b)):
            if b[i] == '*':  # những chỗ là dấu nhân thì thực hiện trước rồi thay vào vị trí đó
                tmp = int(b[i - 1]) * int(b[i + 1])
                idx = i
                break
        del b[idx + 1]
        del b[idx]
        del b[idx - 1]
        b.insert(idx - 1, str(tmp))
    res = int(b[0])
    for i in range(1, len(b), 2):
        if b[i] == '+':
            res += int(b[i + 1])
        elif b[i] == '-':
            res -= int(b[i + 1])
    return res


def change(s):  # thêm dấu ngoặc cho số âm
    res = ''
    for i in s.split():
        if i[0] == '-' and len(i) > 1:
            res += f'({i})'
        else:
            res += i
    return res


res = []
loop(1, str(a[0]))
chk = 0
for i in res:
    if check(i) == m:
        chk = 1
        print(''.join(change(i)), end='')
        print(f'={m}')
if chk == 0:
    print('IMPOSSIBLE')
    