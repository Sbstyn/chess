#           white   black
#pawn       P       p
#knight     N       n
#bishop     B       b
#rook       R       r
#queen      Q       q
#king       K       k

import settable

def moveChecker(toPlace, fromPlace, id):
    if id == "R" or id == "r":
        return isRookValid(toPlace, fromPlace)
    if id == "B" or id == "b":
        return isBishopValid(toPlace, fromPlace)
    if id == "P" or id == "p":
        return isPawnVaild(toPlace, fromPlace, id)
    if id == "Q" or id == "q":
        return isQueenValid(toPlace, fromPlace)
    if id == "K" or id == "k":
        return isKingValid(toPlace, fromPlace)
    if id == "N" or id == "n":
        return isKnightValid(toPlace, fromPlace)

"""def kingmoves(n):
    if n == -1:
        return allkingmoves
    else:
        allkingmoves = n"""

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

def isKnightValid(toPlace, fromPlace):
    if toPlace == fromPlace - 2 + 8 or toPlace == fromPlace - 2 - 8:
        if knightEdgeCheck(f=fromPlace, t=toPlace) > 2:
            return True
    if toPlace == fromPlace - 16 + 1 or toPlace == fromPlace - 16 - 1:
        if knightEdgeCheck(f=fromPlace, t=toPlace) > 2:
            return True
    if toPlace == fromPlace + 2 + 8 or toPlace == fromPlace + 2 - 8:
        if knightEdgeCheck(f=fromPlace, t=toPlace) > 1:
            return True
    if toPlace == fromPlace + 16 + 1 or toPlace == fromPlace + 16 - 1:
        if knightEdgeCheck(f=fromPlace, t=toPlace) > 1:
            return True
    return False

def isKingValid(toPlace, fromPlace):
    if fromPlace - toPlace == 9 or  fromPlace - toPlace == 1 or fromPlace - toPlace == -7:
        if rookEdgeCheck(t=toPlace,f=fromPlace) > 1:
            settable.kingmoves[0] += 1
            return True
    if fromPlace - toPlace == -9 or fromPlace - toPlace == -1 or fromPlace - toPlace == 7:
        if rookEdgeCheck(t=toPlace,f=fromPlace) > 1:
            settable.kingmoves[0] += 1
            return True
    if fromPlace - toPlace == 8 or fromPlace - toPlace == -8:
        settable.kingmoves[0] += 1
        return True
    return False

def isQueenValid(toPlace, fromPlace):
    if isRookValid(fromPlace=fromPlace, toPlace=toPlace) == True:
        print("r")
        return True
    if isBishopValid(fromPlace=fromPlace, toPlace=toPlace) == True:
        print("b")
        return True
    return False

def isPawnVaild(toPlace, fromPlace, id):
    if id == "P":
        if(fromPlace - toPlace == 8):
            return True
        for x in range(0, 8):
            if(fromPlace == 49 + x and fromPlace - toPlace == 16):
                return True
        return False
    if id == "p":
        if(toPlace - fromPlace == 8):
            return True
        for x in range(0, 8):
            if(fromPlace == 9 + x and toPlace - fromPlace == 16):
                return True
        return False

def rookEdgeCheck(f, t):
    if(t>f):
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(8 - x + 1)
                    return 8 - x + 1
    else:
        for x in range(1, 9):
            for y in range(0, 8):
                if(f == x + y * 8):
                    print(x)
                    return x
    return False

def isRookValid(toPlace, fromPlace):
    for x in range(1, 8):
        if(fromPlace + 8 * x == toPlace):
            return True
    for x in range(1, 8):
        if(fromPlace - 8 * x == toPlace):
            return True

    for x in range(1, rookEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace + 1 * x == toPlace):
            return True
    for x in range(1, rookEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace - 1 * x == toPlace):
            return True
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

def isBishopValid(toPlace, fromPlace):
    #if(isRookValid(toPlace=toPlace, fromPlace=fromPlace) == True):
    #    return False
    #print(edgeCheck(f=fromPlace, t=toPlace))
    if(bishopEdgeCheck(f=fromPlace, t=toPlace) == False):
        return False
    for x in range(1, bishopEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace + 7 * x == toPlace):
            #return (edgeCheck(f = fromPlace + 7 * x))
            return True
    for x in range(1, bishopEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace - 7 * x == toPlace):
            return True
    
    for x in range(1, bishopEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace + 9 * x == toPlace):
            return True
    for x in range(1, bishopEdgeCheck(f=fromPlace, t=toPlace)):
        if(fromPlace - 9 * x == toPlace):
            return True
    
    return False

#print(isRookValid(fromPlace=18, toPlace=24))
