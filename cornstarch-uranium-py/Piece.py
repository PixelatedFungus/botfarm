import Exceptions

class Piece():
    def __init__(self, name, square) -> None:
        self.name = name
        self.square = square
    
    def move(self, new_square):
        is_valid = self.check_valid_move(new_square)
        if is_valid:
            self.square = new_square
        else:
            raise Exceptions.InvalidMove