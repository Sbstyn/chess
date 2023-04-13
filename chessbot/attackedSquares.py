import matrix
import checkMove

#square id!

def checkIfSquareAttacked(attackedBy):
    sq_a = []
    for i in range(0, len(matrix.board)):
        #print(checkMove.pawnAttackEdgeCheck(i +1), i +1)
        if (matrix.board[i].isupper() and matrix.board[i] != ".") and attackedBy == "w":
            if matrix.board[i] == "P":
                if checkMove.pawnAttackEdgeCheck(i +1) != -1:
                    if i - 8 + 1 + 1 not in sq_a:
                        sq_a.append(i - 8 + 1 + 1)
                if checkMove.pawnAttackEdgeCheck(i +1) != 1:
                    if i - 8 - 1 + 1 not in sq_a:
                        sq_a.append(i - 8 - 1 + 1)
            if matrix.board[i] == "K":
                print(checkMove.kingEdgeCheck(i, i))

        
        elif (not matrix.board[i].isupper() and matrix.board[i] != ".") and attackedBy == "b":
            if matrix.board[i] == "p":
                if checkMove.pawnAttackEdgeCheck(i +1) != 1:
                    if i + 8 - 1 + 1 not in sq_a:
                        sq_a.append(i + 8 - 1 + 1)
                if checkMove.pawnAttackEdgeCheck(i +1) != -1:
                    if i + 8 + 1 + 1 not in sq_a:
                        sq_a.append(i + 8 + 1 + 1)
    return sq_a

print(checkIfSquareAttacked("b"), checkIfSquareAttacked("w"), sep="\n")
matrix.pBoard()
