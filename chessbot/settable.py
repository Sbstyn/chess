import matrix
#from checkMove import checkIfSquareAttacked

#0:w 1:b
turn = [0]
#bw
kingmoves = [0,0]
#bl br wl wr
rookmoves = [0,0,0,0]
#able to move to
enpassant = [0]

def settable(st):
    kingmoves[0] = 0
    st = str(st)
    if st == "set":
        st = "8" * 8
        updateBoard(st=st)
        st = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        updateBoard(st=st)
        for s in range(0, len(rookmoves)):
            rookmoves[s] = 0
        for s in range(0, len(kingmoves)):
            kingmoves[s] = 0
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
        a = a[:-1]

        if turn[0] == 1:
            t = "b"
        else:
            t = "w"

        cas = ""
        if rookmoves[3] == 0:
            cas += "K"
        if rookmoves[2] == 0:
            cas += "Q"
        if rookmoves[1] == 0:
            cas += "k"
        if rookmoves[0] == 0:
            cas += "q"

        a += f" {t} {cas}"
        print(a)
        
    elif st == "movesdata":
        print(kingmoves, rookmoves, enpassant)
    
    #elif st == "att" or st == "attackedsquares":
    #    print(checkIfSquareAttacked("w"), checkIfSquareAttacked("b"), sep="\n")

    elif st == "stop" or st == "q":
        quit()

    elif st == "clear":
        st = "8" * 8
        updateBoard(st=st)
        
    elif st.split()[0] == "set":
        x = st.split()[1:]
        print(x)

        if(x[1] == "b"):
            turn[0] = 1
        else:
            turn[0] = 0

        for i in range(0, 4):
            rookmoves[i] = 1

        if "q" in x[2]:
            rookmoves[0] = 0
        if "k" in x[2]:
            rookmoves[1] = 0
        if "Q" in x[2]:
            rookmoves[2] = 0
        if "K" in x[2]:
            rookmoves[3] = 0

        print(f"{x[2]} {st} {rookmoves}")

        updateBoard(st=x[0])

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

        