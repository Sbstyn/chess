import checkMove
import matrix

aray = ["a", "b", "c", "d", "e", "f", "g", "h"]

def getInput():
    i = input()

    if(len(i) == 4):
        pos1 = aray.index(i[0]) + 1 + (56 - 8 * (int(i[1]) - 1))
        pos2 = aray.index(i[2]) + 1 + (56 - 8 * (int(i[3]) - 1))
        
        id = matrix.board[matrix.idboard.index(pos1)]
        print(f"{id}, {pos1}, {pos2}")
        if(checkMove.moveChecker(fromPlace=pos1, toPlace=pos2, id=id) == True):
            print(f"{id}, {pos1}, {pos2}")
            matrix.board[matrix.idboard.index(pos1)] = 0
            matrix.board[matrix.idboard.index(pos2)] = id
        else:
            print("MoveNotLegal")
    matrix.pBoard()
    getInput()

matrix.pBoard()
getInput()

#i = i.rsplit()
#print(i)
