#           white   black
#pawn       P       p
#knight     N       n
#bishop     B       b
#rook       R       r
#queen      Q       q
#king       K       k

import settable
import matrix

def moveChecker(toPlace, fromPlace, id):
    if id == "R" or id == "r":
        if isRookValid(toPlace, fromPlace, id):
            if fromPlace == 1:
                settable.rookmoves[0] = 1
            if fromPlace == 8:
                settable.rookmoves[1] = 1
            if fromPlace == 57:
                settable.rookmoves[2] = 1
            if fromPlace == 64:
                settable.rookmoves[3] = 1
            return True
        else:
            return False
    if id == "B" or id == "b":
        return isBishopValid(toPlace, fromPlace, id)
    if id == "P" or id == "p":
        return isPawnVaild(toPlace, fromPlace, id, n=None)
    if id == "Q" or id == "q":
        return isQueenValid(toPlace, fromPlace, id)
    if id == "K" or id == "k":
        return isKingValid(toPlace, fromPlace, id)
    if id == "N" or id == "n":
        return isKnightValid(toPlace, fromPlace, id)

def knightEdgeCheck(f,t):
    for x in range(1, 9):
        for y in range(0, 8):
            if f == x + y * 8:
                xf = x
    for x in range(1, 9):
        for y in range(0, 8):
            if t == x + y * 8:
                xt = x

    if xf > xt:
        return xf
    else:
        return 8 - xf + 1

def isKnightValid(toPlace, fromPlace, id):
    if ((id == str(id).lower() and str(matrix.board[toPlace -1]).lower() == matrix.board[toPlace -1]) or (id == str(id).upper() and str(matrix.board[toPlace -1]).upper() == matrix.board[toPlace -1])) and matrix.board[toPlace -1] != ".":
        return False
    else:
        print(matrix.board[toPlace -1], knightEdgeCheck(f=fromPlace, t=toPlace))
        if toPlace == fromPlace - 2 + 8 or toPlace == fromPlace - 2 - 8:
            if knightEdgeCheck(f=fromPlace, t=toPlace) > 2:
                return True
        if toPlace == fromPlace - 16 + 1 or toPlace == fromPlace - 16 - 1:
            if knightEdgeCheck(f=fromPlace, t=toPlace) > 1:
                return True
        if toPlace == fromPlace + 2 + 8 or toPlace == fromPlace + 2 - 8:
            if knightEdgeCheck(f=fromPlace, t=toPlace) > 2:
                return True
        if toPlace == fromPlace + 16 + 1 or toPlace == fromPlace + 16 - 1:
            if knightEdgeCheck(f=fromPlace, t=toPlace) > 1:
                return True
    return False

def kingEdgeCheck(f, t):
    for x in range(1, 9):
        for y in range(0, 8):
            if(f == x + y * 8):
                fx = x
    for x in range(1, 9):
        for y in range(0, 8):
            if(t == x + y * 8):
                tx = x
    if tx > fx:
        if tx - fx > 1:
            return 0
        return 2
    else:
        if fx - tx > 1:
            return 0
        return 2

def isKingValid(toPlace, fromPlace, id):
    if id == "K":
        color = 1
    else:
        color = 0
    if ((id == str(id).lower() and str(matrix.board[toPlace -1]).lower() == matrix.board[toPlace -1]) or (id == str(id).upper() and str(matrix.board[toPlace -1]).upper() == matrix.board[toPlace -1])) and matrix.board[toPlace -1] != ".":
        return False
    elif settable.kingmoves[color] == 0 and toPlace == 63:
        if settable.rookmoves[3] == 0 and matrix.board[62 - 1] == "." and matrix.board[63 - 1] == ".":
            matrix.board[64 - 1] = "."
            matrix.board[62 - 1] = "R"
            return True
    else:
        print(f"   {kingEdgeCheck(t=toPlace,f=fromPlace)}")
        if fromPlace - toPlace == 9 or fromPlace - toPlace == 1 or fromPlace - toPlace == -7:
            if kingEdgeCheck(t=toPlace,f=fromPlace) > 1:
                settable.kingmoves[color] += 1
                return True
        if fromPlace - toPlace == -9 or fromPlace - toPlace == -1 or fromPlace - toPlace == 7:
            if kingEdgeCheck(t=toPlace,f=fromPlace) > 1:
                settable.kingmoves[color] += 1
                return True
        if fromPlace - toPlace == 8 or fromPlace - toPlace == -8:
            settable.kingmoves[color] += 1
            return True
        return False

def isQueenValid(toPlace, fromPlace, id):
    for x in range(1, 9):
        for y in range(0, 8):
            if(fromPlace == x + y * 8):
                fx = x
                fy = y
    for x in range(1, 9):
        for y in range(0, 8):
            if(toPlace == x + y * 8):
                tx = x
                ty = y
    if tx == fx or ty == fy:
        if isRookValid(fromPlace=fromPlace, toPlace=toPlace, id=id) == True:
            print("r")
            return True
    else:
        if isBishopValid(fromPlace=fromPlace, toPlace=toPlace, id=id) == True:
            print("b")
            return True
    return False

def isPawnPromotionVaild(toPlace, fromPlace, id, n):
    l = ["N", "Q", "R", "B"]
    if id == str(id).lower():
        if str(n).upper() in l:
            print("l")
        else:
            return False
    elif id == str(id).upper():
        if n in l:
            print("u")
        else:
            return False
    else:    
        return False
    for x in range(0, 8):
        if toPlace == 1 + x or toPlace == 57 + x:
            print(toPlace, True)
            if isPawnVaild(toPlace=toPlace, fromPlace=fromPlace, id=id, n=n) == True:
                print(True)
                return True
    return False

def isPawnVaild(toPlace, fromPlace, id, n):
    if n == None:
        for x in range(0,8):
            if toPlace == x + 1 or toPlace == x + 57:
                return False
    if id == "P" and (matrix.board[toPlace - 1] == "." or matrix.board[toPlace - 1].lower() == matrix.board[toPlace - 1]):
        if(fromPlace - toPlace == 8):
            if matrix.board[toPlace - 1] == ".":
                print(matrix.board[toPlace - 1])
                return True
            else:
                return False
        if (fromPlace - toPlace == 7 or fromPlace - toPlace == 9) and matrix.board[toPlace - 1] != ".":
            return True
        for x in range(0, 8):
            if(fromPlace == 49 + x and fromPlace - toPlace == 16):
                return True
        return False
    if id == "p" and (matrix.board[toPlace - 1] == "." or matrix.board[toPlace - 1].upper() == matrix.board[toPlace - 1]):
        if(fromPlace - toPlace == -8):
            if matrix.board[toPlace - 1] == ".":
                print(matrix.board[toPlace - 1])
                return True
            else:
                return False
        if (fromPlace - toPlace == -7 or fromPlace - toPlace == -9) and matrix.board[toPlace - 1] != ".":
            return True
        for x in range(0, 8):
            if(fromPlace == 9 + x and fromPlace - toPlace == -16):
                return True

def rookEdgeCheck(f, t):
    if(t>f):
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    #print(8 - x + 1)
                    return 8 - x + 1
    else:
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(x)
                    return x
    return False

def isRookValid(toPlace, fromPlace, id):
    try:
        for x in range(1, 9):
            for y in range(0, 8):
                if(fromPlace == x + y * 8):
                    fx = x
        for x in range(1, 9):
            for y in range(0, 8):
                if(toPlace == x + y * 8):
                    tx = x

        if tx == fx:
            if toPlace > fromPlace:
                return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=8, f=8)
            else:
                return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=-8, f=8)

        if toPlace > fromPlace:
            return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=1, f=rookEdgeCheck(f=fromPlace, t=toPlace))
        else:
            return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=-1, f=rookEdgeCheck(f=fromPlace, t=toPlace))

    except:
        print("err")
        return False

def bishopEdgeCheck(f, t):
    print(f"/7 {(f - t) % 7}, /9 {(f - t) % 9}")
    if((f - t) % 7 == 0 and (f - t) % 9 == 0):
        print("-1")
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(x + y * 8)
                    print(f"able to move: {8 - x + 1}")
                    return 8 - x + 1
    
    if(((f - t) % 7 == 0 and t > f) or ((f - t) % 9 == 0 and t < f)):
        print("0")
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(x)
                    return x
    else:
        print("1")
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(x + y * 8)
                    print(f"able to move: {8 - x + 1}")
                    return 8 - x + 1
    return False

def isBishopValid(toPlace, fromPlace, id):
    if(bishopEdgeCheck(f=fromPlace, t=toPlace) == False):
        return False
    for x in range(1, 9):
        for y in range(0, 8):
            if(fromPlace == x + y * 8):
                fx = x
                fy = y
    for x in range(1, 9):
        for y in range(0, 8):
            if(toPlace == x + y * 8):
                tx = x
                ty = y
    if tx < fx and ty > fy:
        return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=7, f=bishopEdgeCheck(f=fromPlace, t=toPlace))
    if tx > fx and ty < fy:
        return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=-7, f=bishopEdgeCheck(f=fromPlace, t=toPlace))
    if tx > fx and ty > fy:
        return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=9, f=bishopEdgeCheck(f=fromPlace, t=toPlace))
    if tx < fx and ty < fy:
        return stopCheck(toPlace=toPlace, fromPlace=fromPlace, id=id, move=-9, f=bishopEdgeCheck(f=fromPlace, t=toPlace))
    
    return False

def stopCheck(toPlace, fromPlace, id, move, f):
    for x in range(1, f):
        print(f"{x} {toPlace} {fromPlace} {id} {move} {f}")
        if ((id == str(id).lower() and str(matrix.board[fromPlace + move * x -1]).lower() == matrix.board[fromPlace + move * x -1]) or (id == str(id).upper() and str(matrix.board[fromPlace + move * x -1]).upper() == matrix.board[fromPlace + move * x -1])) and matrix.board[fromPlace + move * x -1] != ".":
            print(f"0 {id}, {matrix.board[fromPlace + move * x -1]}")
            return False
        elif matrix.board[fromPlace + move * x -1] != ".":
            print("a")
            #pl = True
            if (fromPlace + move * x == toPlace):
                print("b1")
                return True
            return False
        elif (fromPlace + move * x == toPlace):
            print(f"b2 {fromPlace + move * x}")
            return True

#print(isRookValid(fromPlace=18, toPlace=24))
