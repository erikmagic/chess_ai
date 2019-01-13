import chess

class Minimax_player:
    '''
    this class maintains an internal representation of the chess board
    and is queried to decide on a move
    '''
   
    def __init__(self, color, board):
        self.board = board
        self.color = color
        if color == chess.WHITE:
            self.move()
    
    def move(self, move):
        pass

    def heuristic_fct(self):
        '''
        the components of the heuristic functions are the following
        1. differences in pieces between self and opponent
        2. control of the middle
        3. position of the pawns
        4. number of possible moves
        each of these components are weighted by coefficients
        '''
        # get the list of current pieces
        

    PIECE_VALUES = {
        "p": 1,
        "n": 3,
        "b": 3,
        "r": 5,
        "q": 9,
        "k": 0
    }
    def retrieve_piece_values(self):
        pieces = self.board.piece_map()
        my_piece_values, opp_piece_values = 0, 0
        for piece in pieces:
            if piece.color == chess.WHITE:
                if self.color == chess.WHITE:
                    my_piece_values += self.PIECE_VALUES[piece.symbol().lower()]
                else:
                    opp_piece_values += self.PIECE_VALUES[piece.symbol().lower()]
            else:
                if self.color == chess.BLACK:
                    my_piece_values += self.PIECE_VALUES[piece.symbol().lower()]
                else:
                    opp_piece_values += self.PIECE_VALUES[piece.symbol().lower()]
                
        return my_piece_values - opp_piece_values

    def retrieve_position_strength(self):
        pass        

