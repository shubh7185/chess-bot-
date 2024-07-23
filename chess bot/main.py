import chess as ch
import ChessEngine as ce  # Ensure this matches the filename and class name

class Main:
    def __init__(self, board=None):
        self.board = board or ch.Board()

    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            move = input("Your move: ")
            if move == "undo":
                if len(self.board.move_stack) >= 2:
                    self.board.pop()
                    self.board.pop()
                else:
                    print("Not enough moves to undo.")
                self.playHumanMove()
                return
            self.board.push_san(move)
        except Exception as e:
            print(f"Error: {e}")
            self.playHumanMove()

    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        best_move = engine.getBestMove()
        if best_move:
            self.board.push(best_move)

    def startGame(self):
        color = None
        while color not in ["b", "w"]:
            color = input('Play as (type "b" or "w"): ')
        maxDepth = None
        while not isinstance(maxDepth, int):
            try:
                maxDepth = int(input("Choose depth: "))
            except ValueError:
                print("Please enter a valid integer.")

        if color == "b":
            while not self.board.is_checkmate():
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
        elif color == "w":
            while not self.board.is_checkmate():
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)

        print(self.board)
        print(self.board.outcome())
        self.board.reset()
        self.startGame()

# Create an instance and start a game
if __name__ == "__main__":
    game = Main()
    game.startGame()
