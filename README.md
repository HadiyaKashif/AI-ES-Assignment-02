CODE EXPLANATION:
Part 1: Utility Functions & Game Setup
This part defines the foundation of the game:
•	INITIAL_STATE(): Creates a blank 3x3 board.
•	PLAYER(): Determines whose turn it is (alternates between 'O' and 'X').
•	ACTIONS(): Lists available moves.
•	RESULT(): Returns the new board after a move is applied.
•	TERMINAL(): Checks if the game is over.
•	UTILITY(): Assigns score based on winner (10 for AI, -10 for Human, 0 for Draw).
•	WINNER(): Checks rows, columns, and diagonals for a winner.
•	DISPLAY(): Prints the board in a readable format.
Part 2: Minimax Algorithm 
This part implements the basic Minimax algorithm, which simulates all possible future moves:
•	MAX_VALUE() and MIN_VALUE() recursively evaluate the board from AI and Human perspectives.
•	MINIMAX_DECISION(): Chooses the best move for AI by simulating opponent’s responses.
Part 3: Minimax with Alpha-Beta Pruning
This part optimizes Minimax using alpha-beta pruning:
•	MAX_VALUE_AB() and MIN_VALUE_AB() cut off branches that won’t affect final decision using alpha (max lower bound) and beta (min upper bound).
•	MINIMAX_AB_DECISION(): AI selects move using the faster pruned search.
Part 4: Game Playing Function
This part handles the gameplay loop:
•	Alternates between Human and AI turns.
•	Accepts input from human (if enabled).
•	Calls the selected AI function (Minimax or Alpha-Beta).
•	Tracks and prints time taken by AI.
•	Displays board after each move and announces result at the end.
Part 5: Game Comparison
Runs both AIs automatically and compares their speed:
•	COMPARE_FULL_GAME() plays two full games: one with Minimax, one with Alpha-Beta.
•	Displays time taken by each algorithm and prints a comparison summary.

Minimax vs Alpha-Beta Pruning:
Feature	Minimax	Alpha-Beta
Speed	Slower	Faster due to pruning
Logic	Explores full tree	Skips unnecessary branches
Result	Same move quality	Same move quality
Best Use	Teaching, brute-force check	Real-time AI decisions
 
