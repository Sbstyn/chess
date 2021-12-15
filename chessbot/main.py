import checkMove
import matrix
import settable

aray = ["a", "b", "c", "d", "e", "f", "g", "h"]

def getInput():
    i = input()

    if i[0] == "-":
        settable.settable(i[1:])
    elif(len(i) == 4):
        pos1 = aray.index(i[0]) + 1 + (56 - 8 * (int(i[1]) - 1))
        pos2 = aray.index(i[2]) + 1 + (56 - 8 * (int(i[3]) - 1))
        
        id = matrix.board[matrix.idboard.index(pos1)]
        print(f"{id}, {pos1}, {pos2}")
        if(pos1 != pos2 and checkMove.moveChecker(fromPlace=pos1, toPlace=pos2, id=id) == True):
            print(f"{id}, {pos1}, {pos2}")
            matrix.board[matrix.idboard.index(pos1)] = "."
            matrix.board[matrix.idboard.index(pos2)] = id
        else:
            print("MoveNotLegal")
    #elif

    print(settable.kingmoves[0])
    
    matrix.pBoard()
    getInput()

matrix.pBoard()
getInput()

#i = i.rsplit()
#print(i)
