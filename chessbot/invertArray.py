"""def inv(a):
    b = []
    print(len(a))
    for i in range(len(a), 0, -1):
        b.append(a[i - 1])
    print(b)

#for i in range(8, 0, -1):
#    print(i)

inv(["a", "b", "c", "d", "e", "f", "g", "h"])"""


st = "asd4dsa"
for i in range(1, len(st)):
    try:
        int(st[i])
        st = st.replace(st[i], "0" * int(st[i]))
        print(st)
    except:
        print("-", end="")