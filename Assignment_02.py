import math
import copy
import time

EMPTY = ' '
HUMAN = 'O'
AI = 'X'

# ===== Part 1: Utility Functions, Game Setup =====
def INITIAL_STATE():
    return [[EMPTY for _ in range(3)] for _ in range(3)]
def PLAYER(board):
    flat = sum(board, [])
    return AI if flat.count(AI) == flat.count(HUMAN) else HUMAN
def ACTIONS(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
def RESULT(board, action, player):
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player
    return new_board
def TERMINAL(board):
    return WINNER(board) is not None
def UTILITY(board):
    winner = WINNER(board)
    if winner == AI:
        return 10
    elif winner == HUMAN:
        return -10
    else:
        return 0
def WINNER(board):
    lines = board + list(zip(*board)) + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != EMPTY:
            return line[0]
    if all(cell != EMPTY for row in board for cell in row):
        return 'Draw'
    return None
def DISPLAY(board):
    print("\nBoard:")
    for row in board:
        print(' | '.join(row))
        print('-' * 9)
# ==========================================

# ===== Part 2: Minimax Algorithm =====
# Basic recursive algorithm without optimization
def MAX_VALUE(board):
    if TERMINAL(board):
        return UTILITY(board)
    v = -math.inf
    for action in ACTIONS(board):
        v = max(v, MIN_VALUE(RESULT(board, action, AI)))
    return v

def MIN_VALUE(board):
    if TERMINAL(board):
        return UTILITY(board)
    v = math.inf
    for action in ACTIONS(board):
        v = min(v, MAX_VALUE(RESULT(board, action, HUMAN)))
    return v

def MINIMAX_DECISION(board):
    best_score = -math.inf
    best_move = None
    for action in ACTIONS(board):
        score = MIN_VALUE(RESULT(board, action, AI))
        if score > best_score:
            best_score = score
            best_move = action
    return best_move
# ==========================================

# ===== Part 3: Alpha-Beta Pruning =====
# Faster version of Minimax using pruning
def MAX_VALUE_AB(board, alpha, beta):
    if TERMINAL(board):
        return UTILITY(board)
    v = -math.inf
    for action in ACTIONS(board):
        v = max(v, MIN_VALUE_AB(RESULT(board, action, AI), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def MIN_VALUE_AB(board, alpha, beta):
    if TERMINAL(board):
        return UTILITY(board)
    v = math.inf
    for action in ACTIONS(board):
        v = min(v, MAX_VALUE_AB(RESULT(board, action, HUMAN), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def MINIMAX_AB_DECISION(board):
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for action in ACTIONS(board):
        score = MIN_VALUE_AB(RESULT(board, action, AI), alpha, beta)
        if score > best_score:
            best_score = score
            best_move = action
        alpha = max(alpha, best_score)
    return best_move
# ==========================================

# ===== Part 4: Game Playing =====
def PLAY_GAME(ai_func, title="AI", human=False):
    board = INITIAL_STATE()
    DISPLAY(board)
    total_time = 0
    while not TERMINAL(board):
        current_player = PLAYER(board)
        if current_player == HUMAN and human:
            try:
                print("\nYour turn! Enter move (row and column):")
                i = int(input("Row (0-2): "))
                j = int(input("Col (0-2): "))
                if (i, j) not in ACTIONS(board):
                    print("Invalid move. Try again.")
                    continue
                board = RESULT(board, (i, j), HUMAN)
            except ValueError:
                print("Invalid input. Try again.")
                continue
        else:
            print(f"\n{title} is thinking...")
            start = time.time()
            move = ai_func(board)
            end = time.time()
            total_time += end - start
            board = RESULT(board, move, current_player)
            print(f"{title} played: {move}")
        DISPLAY(board)
    result = WINNER(board)
    if result == 'Draw':
        print("\nIt's a draw!")
    else:
        print(f"\n{result} wins!")
    print(f"Total Time for {title}: {total_time:.5f} sec\n")
    return total_time
# ==========================================

# ===== Part 5: Game Comparison =====
def COMPARE_FULL_GAME():
    print("=== Running Full Game with Basic Minimax ===")
    minimax_time = PLAY_GAME(MINIMAX_DECISION, title="Minimax AI", human=False)

    print("=== Running Full Game with Alpha-Beta Pruning ===")
    alphabeta_time = PLAY_GAME(MINIMAX_AB_DECISION, title="Alpha-Beta AI", human=False)

    print("=== Comparison Summary ===")
    print(f"Minimax Time: {minimax_time:.5f} sec")
    print(f"Alpha-Beta Time: {alphabeta_time:.5f} sec")
# ==========================================

# ===== Part 6: Main Function =====
if __name__ == "__main__":
    print("Choose mode:")
    print("1 - Human vs Alpha-Beta AI")
    print("2 - Human vs Minimax AI")
    print("3 - Full Auto Comparison (Minimax vs Alpha-Beta)")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        PLAY_GAME(MINIMAX_AB_DECISION, title="Alpha-Beta AI", human=True)
    elif choice == '2':
        PLAY_GAME(MINIMAX_DECISION, title="Minimax AI", human=True)
    elif choice == '3':
        COMPARE_FULL_GAME()
    else:
        print("Invalid choice.")
# ==========================================