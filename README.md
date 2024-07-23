
# Chess Bot

A chess bot that allows a human player to play against an AI engine using the chess library and a simple min-max algorithm with alpha-beta pruning for decision-making.

## Project Overview

This project includes:
- **A chess bot**: An AI engine that plays chess against a human player.
- **A command-line interface**: Allows users to play against the chess bot, make moves, undo moves, and reset the game.
- **A chess engine**: Uses a basic evaluation function to determine the best moves.

## Files

2. **`main.py`**: Contains the `Main` class for managing the game, including human and engine moves.
3. **`ChessEngine.py`**: Contains the `Engine` class implementing the chess AI with min-max algorithm and evaluation functions.

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    Make sure `requirements.txt` is properly created with necessary dependencies. If it’s not present, manually install the required packages:

    ```sh
    pip install chess
    ```

## Usage

1. **Run the Chess Bot:**

    ```sh
    python main.py
    ```

    This will start a new game where you can play against the AI bot. You will be prompted to:
    - Choose your color (`b` for black, `w` for white).
    - Set the depth of the AI's search.
    - Make your move in standard algebraic notation.
    - Undo moves if needed.
    - Play until checkmate or draw.

2. **Run the Streamlit App (if applicable):**

    If you switch to Streamlit, ensure `app.py` is correctly set up and run it with:

    ```sh
    streamlit run app.py
    ```

## Code Overview

### `main.py`

- **`Main` Class**: Manages game flow, human player moves, and engine moves.
- **Methods**:
  - `playHumanMove()`: Handles user input for moves and undo functionality.
  - `playEngineMove(maxDepth, color)`: Makes the AI move based on the depth and color.
  - `startGame()`: Initializes the game, handles turns, and restarts the game after it ends.

### `ChessEngine.py`

- **`Engine` Class**: Implements the chess AI using min-max algorithm with alpha-beta pruning.
- **Methods**:
  - `getBestMove()`: Returns the best move calculated by the AI.
  - `evalFunct()`: Evaluates the board position.
  - `mateOpportunity()`: Evaluates potential checkmate opportunities.
  - `openning()`: Encourages development in the opening moves.
  - `squareResPoints(square)`: Assigns a value to a piece based on its type and position.
  - `engine(candidate, depth)`: Recursively evaluates moves using min-max algorithm with alpha-beta pruning.

## Contributing

Contributions are welcome! Please submit pull requests or issues with details of your changes or improvements.


---

Feel free to customize this README according to your project’s specifics and needs. Let me know if you need any more details or adjustments!
