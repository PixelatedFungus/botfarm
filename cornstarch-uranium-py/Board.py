import json
class Board():
    
    def __init__(self) -> None:
        self.createBoard()

    def createBoard(self) -> None:
        with open("initial_board.json", "r") as json_file:
            self.board = json.load(json_file)
        json_file.close()

    def getPiece(self, square) -> str:
        return self.board[square]['piece']

    def getBoard(self) -> list:
        return self.board
    
    def getColor(self, square) -> str:
        return self.board[square]['square_color']
    
    def checkScan(self):
        pass
                
    def translateLetterToNumber(self, column) -> int:
        match column:
            case 'A':
                return 1
            case 'B':
                return 2
            case 'C':
                return 3
            case 'D':
                return 4
            case 'E':
                return 5
            case 'F':
                return 6
            case 'G':
                return 7
            case 'H':
                return 8