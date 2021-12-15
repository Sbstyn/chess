import matrix

kingmoves = [0]

def settable(st):
    kingmoves[0] = 0
    st = str(st)
    if st == "set":
        st = "8" * 8
        updateBoard(st=st)
        st = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        updateBoard(st=st)
    elif st == "fen":
        zer = False
        z = 0
        a = ""
        x = 1
        for m in matrix.board:
            if m == "0" or m == ".":
                zer = True
                z += 1
            else:
                if zer == True:
                    zer = False
                    a += str(z)
                    z = 0
                a += m
            if x % 8 == 0:
                if z != 0:
                    a += str(z)
                    z = 0
                    zer = False
                a += "/"
            
            x += 1
        print(a)
        
    elif st == "clear":
        st = "8" * 8
        updateBoard(st=st)
        
    elif st[0] == "x":
        st = st[1:]
        """while "/" in st:
            st = st.replace("/", "")"""

        print(st)

        updateBoard(st=st)
        """n = ""
        for a in range(0, len(st)):
            if st[a].isnumeric():
                if int(st[a]) != 0:
                    n += "0" * int(st[a])
            else:
                print("-", end="")
                n += st[a]

        print(f"\n{n}")
        for i in range(0,len(n)):
            matrix.board[i] = n[i]"""
    #matrix.pBoard()

def updateBoard(st):
    while "/" in st:
        st = st.replace("/", "")

    n = ""
    for a in range(0, len(st)):
        if st[a].isnumeric():
            if int(st[a]) != 0:
                n += "." * int(st[a])
        else:
            print("-", end="")
            n += st[a]
    print(f"{len(n)} {len(matrix.board)}")
    for i in range(0,len(n)):
        matrix.board[i] = n[i]

#settable("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
#rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR