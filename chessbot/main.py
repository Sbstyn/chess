import checkMove
import matrix
import commands
from math import floor

"""
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
r1bqk2r/pppp1ppp/1bn2n2/8/4P3/1NNB4/PPP2PPP/R1BQ1RK1 b kq - 1 1
r1bq1rk1/pppp1ppp/1bn2n2/8/4P3/1NNB4/PPP2PPP/R1BQ1RK1 w - - 2 2
rnbqkbnr/pppp2pp/5p2/4p3/4P2P/7R/PPPP1PP1/RNBQKBN1 b Qkq - 1 3

castling
rnbqk2r/ppppppbp/5np1/8/8/5NP1/PPPPPPBP/RNBQK2R w KQkq - 4 4
"""

def start():
    aray = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def getInput():
        i = input()

        if i[0] == "-":
            commands.prompt(i[1:])
        elif(len(i) == 4):
            pos1 = aray.index(i[0]) + 1 + (56 - 8 * (int(i[1]) - 1))
            pos2 = aray.index(i[2]) + 1 + (56 - 8 * (int(i[3]) - 1))
            
            id = matrix.board[matrix.idboard.index(pos1)]
            print(f"{id}, {pos1}, {pos2}")
            if(pos1 != pos2 and checkMove.moveChecker(fromPlace=pos1, toPlace=pos2, id=id) == True):
                #t
                if pos2 == 1:
                    commands.rookmoves[0] = 1
                if pos2 == 8:
                    commands.rookmoves[1] = 1
                if pos2 == 57:
                    commands.rookmoves[2] = 1
                if pos2 == 64:
                    commands.rookmoves[3] = 1
                print(f"{id}, {pos1}, {pos2}")
                matrix.board[matrix.idboard.index(pos1)] = "."
                matrix.board[matrix.idboard.index(pos2)] = id

                commands.moves += 1
                commands.clock = floor(commands.moves / 2) + 1
                if commands.clock % 2 == 0:
                    commands.turn = "w"
                else:
                    commands.turn = "b"
            else:
                print("Error code: 1")
        
        elif len(i) == 5:
            pos1 = aray.index(i[0]) + 1 + (56 - 8 * (int(i[1]) - 1))
            pos2 = aray.index(i[2]) + 1 + (56 - 8 * (int(i[3]) - 1))
            
            id = matrix.board[matrix.idboard.index(pos1)]
            if id == "p" or id == "P":
                print(f"{id}, {pos1}, {pos2}")
                if(pos1 != pos2 and checkMove.isPawnPromotionVaild(fromPlace=pos1, toPlace=pos2, id=id, n=i[4]) == True):
                    print(f"{id}, {pos1}, {pos2}")
                    matrix.board[matrix.idboard.index(pos1)] = "."
                    matrix.board[matrix.idboard.index(pos2)] = i[4]
            else:
                print("MoveNotLegal")

        #print(commands.kingmoves[0])
        
        matrix.pBoard()
        getInput()

    matrix.pBoard()
    getInput()

if __name__ == "__main__":
    start()

#i = i.rsplit()
#print(i)
