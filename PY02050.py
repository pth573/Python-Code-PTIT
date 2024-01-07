for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    ans = [0] * n
    st = []
    for i in range(len(li)):
        tmp = []
        cnt = 1
        while len(st) > 0 and li[i] >= st[-1][0]:
            cnt += st[-1][1]
            st.pop()
        tmp = [li[i], cnt]
        ans[i] = cnt
        st.append(tmp)
    for x in ans:
        print(x, end=" ")
    print()
