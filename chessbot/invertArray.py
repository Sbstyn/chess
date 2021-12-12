"""def inv(a):
    b = []
    print(len(a))
    for i in range(len(a), 0, -1):
        b.append(a[i - 1])
    print(b)

#for i in range(8, 0, -1):
#    print(i)

inv(["a", "b", "c", "d", "e", "f", "g", "h"])"""

for i in range(1, 65):
    if i % 7 == 0 and i % 9 == 0:
        print(i)