import matrix
def settable(st):
    st = str(st)
    if st == "set":
        st = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    elif st == "clear":
        st = "8" * 8

    while "/" in st:
        st = st.replace("/", "")

    print(st)
    for a in range(0, len(st)):
        try:
            int(st[a])
            if int(st[a]) != 0:
                st = st.replace(st[a], "0" * int(st[a]))
        except:
            print("-", end="")
    print()
    for i in range(0,len(st)):
        matrix.board[i] = st[i]
    #matrix.pBoard()


#settable("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR