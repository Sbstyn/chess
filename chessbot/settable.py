import matrix

kingmoves = [0]

def settable(st):
    kingmoves[0] = 0
    st = str(st)
    if st == "set":
        st = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    elif st == "clear":
        st = "8" * 8
        
    while "/" in st:
        st = st.replace("/", "")

    baseSt = ""
    for i in st:
        baseSt += i

    print(st)
    n = ""
    for a in range(0, len(st)):
        if st[a].isnumeric():
            if int(st[a]) != 0:
                n += "0" * int(st[a])
        else:
            print("-", end="")
            n += st[a]

    print(f"\n{n}")
    for i in range(0,len(n)):
        matrix.board[i] = n[i]
    #matrix.pBoard()


#settable("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR