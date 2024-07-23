import chess as ch
import random as rd

class Engine:
    def __init__(self, board, maxDepth, color):
        self.board = board
        self.color = color
        self.maxDepth = maxDepth

    def getBestMove(self):
        return self.engine(None, 1)

    def evalFunct(self):
        score = 0
        for square in ch.SQUARES:
            score += self.squareResPoints(square)
        score += self.mateOpportunity() + self.openning() + 0.001 * rd.random()
        return score

    def mateOpportunity(self):
        if not self.board.legal_moves:
            return 999 if self.board.turn != self.color else -999
        return 0

    def openning(self):
        if self.board.fullmove_number < 10:
            return (1/30 * len(self.board.legal_moves) if self.board.turn == self.color 
                    else -1/30 * len(self.board.legal_moves))
        return 0

    def squareResPoints(self, square):
        piece_type = self.board.piece_type_at(square)
        piece_values = {
            ch.PAWN: 1,
            ch.ROOK: 5.1,
            ch.BISHOP: 3.33,
            ch.KNIGHT: 3.2,
            ch.QUEEN: 8.8
        }
        piece_value = piece_values.get(piece_type, 0)
        return piece_value if self.board.color_at(square) == self.color else -piece_value

    def engine(self, candidate, depth):
        if depth == self.maxDepth or not self.board.legal_moves:
            return self.evalFunct()

        best_value = float("-inf") if depth % 2 != 0 else float("inf")
        best_move = None

        for move in self.board.legal_moves:
            self.board.push(move)
            value = self.engine(best_value, depth + 1)
            self.board.pop()

            if depth % 2 != 0:
                if value > best_value:
                    best_value = value
                    if depth == 1:
                        best_move = move
            else:
                if value < best_value:
                    best_value = value

            if candidate is not None:
                if (depth % 2 != 0 and value > candidate) or (depth % 2 == 0 and value < candidate):
                    break

        return best_move if depth == 1 else best_value
