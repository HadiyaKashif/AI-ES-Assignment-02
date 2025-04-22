
## 🎮 Code Explanation

### 🧩 Part 1: Utility Functions & Game Setup  
This part defines the foundation of the game:

- `initial_state()`: Creates a blank 3x3 board.  
- `player()`: Determines whose turn it is (alternates between `'O'` and `'X'`).  
- `actions()`: Lists all available moves.  
- `result()`: Returns a new board after a move is applied.  
- `terminal()`: Checks if the game is over.  
- `utility()`: Assigns a score based on the winner (10 for AI, -10 for Human, 0 for Draw).  
- `winner()`: Checks rows, columns, and diagonals for a winner.  
- `display()`: Prints the board in a readable format.

---

### 🧠 Part 2: Minimax Algorithm  
This part implements the basic Minimax algorithm, which simulates all possible future moves:

- `max_value()` and `min_value()`: Recursively evaluate the board from AI and Human perspectives.  
- `minimax_decision()`: Chooses the best move for AI by simulating the opponent’s responses.

---

### ⚡ Part 3: Minimax with Alpha-Beta Pruning  
This part optimizes Minimax using alpha-beta pruning:

- `max_value_ab()` and `min_value_ab()`: Skip branches that won’t affect the final decision using `alpha` (max lower bound) and `beta` (min upper bound).  
- `minimax_ab_decision()`: AI selects the best move using the faster pruned search.

---

### 🎮 Part 4: Game Playing Function  
This part handles the gameplay loop:

- Alternates between Human and AI turns.  
- Accepts input from the human (if enabled).  
- Calls the selected AI function (Minimax or Alpha-Beta).  
- Tracks and prints the time taken by AI.  
- Displays the board after each move and announces the result at the end.

---

### 🧪 Part 5: Game Comparison  
This part runs both AIs automatically and compares their performance:

- `compare_full_game()`: Plays two full games — one with Minimax and one with Alpha-Beta.  
- Displays the time taken by each algorithm and prints a comparison summary.

---

## 🤖 Minimax vs Alpha-Beta Pruning

| Feature        | Minimax            | Alpha-Beta Pruning              |
|----------------|--------------------|----------------------------------|
| **Speed**      | Slower             | Faster due to pruning            |
| **Logic**      | Explores full tree | Skips unnecessary branches       |
| **Result**     | Same move quality  | Same move quality                |
| **Best Use**   | Teaching, brute-force check | Real-time AI decisions  |
