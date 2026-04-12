import tkinter as tk
from tkinter import messagebox
from tkinter import font

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.human_first = None
        self.current_player = None
        self.game_over = False
        
        self.show_menu()
    
    def show_menu(self):
        self.clear_window()
        
        title_font = font.Font(family="Helvetica", size=20, weight="bold")
        button_font = font.Font(family="Helvetica", size=14)
        
        title = tk.Label(self.root, text="Tic-Tac-Toe", font=title_font, bg="#f0f0f0")
        title.pack(pady=20)
        
        subtitle = tk.Label(self.root, text="Who goes first?", font=button_font, bg="#f0f0f0")
        subtitle.pack(pady=10)
        
        human_btn = tk.Button(
            self.root, text="I Go First (X)", font=button_font, 
            bg="#4CAF50", fg="white", width=20, height=2,
            command=lambda: self.start_game(True)
        )
        human_btn.pack(pady=10)
        
        ai_btn = tk.Button(
            self.root, text="AI Goes First (O)", font=button_font,
            bg="#2196F3", fg="white", width=20, height=2,
            command=lambda: self.start_game(False)
        )
        ai_btn.pack(pady=10)
    
    def start_game(self, human_first):
        self.human_first = human_first
        self.current_player = 'X' if human_first else 'O'
        self.game_over = False
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.show_game_board()
        
        if not human_first:
            self.root.after(500, self.ai_move)
    
    def show_game_board(self):
        self.clear_window()
        
        button_font = font.Font(family="Helvetica", size=18, weight="bold")
        
        # Status label
        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.status_label.pack(pady=10)
        self.update_status()
        
        # Board frame
        board_frame = tk.Frame(self.root, bg="#f0f0f0")
        board_frame.pack(pady=20)
        
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    board_frame, text=' ', font=button_font, width=5, height=3,
                    bg="#e0e0e0", command=lambda row=i, col=j: self.human_click(row, col)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        # Reset button
        reset_btn = tk.Button(
            self.root, text="New Game", font=("Helvetica", 12),
            bg="#FF9800", fg="white", width=15,
            command=self.show_menu
        )
        reset_btn.pack(pady=10)
    
    def update_status(self):
        if self.game_over:
            return
        
        winner = self.check_winner()
        if winner == 'X':
            self.status_label.config(text="You Win!", fg="green")
            self.game_over = True
        elif winner == 'O':
            self.status_label.config(text="AI Wins!", fg="red")
            self.game_over = True
        elif self.is_full():
            self.status_label.config(text="It's a Draw!", fg="blue")
            self.game_over = True
        else:
            if self.current_player == 'X':
                self.status_label.config(text="Your turn (X)", fg="black")
            else:
                self.status_label.config(text="AI is thinking... (O)", fg="black")
    
    def human_click(self, row, col):
        if self.game_over or self.current_player != 'X':
            return
        
        if self.board[row][col] == ' ':
            self.board[row][col] = 'X'
            self.update_board_display()
            self.update_status()
            
            if not self.game_over:
                self.current_player = 'O'
                self.update_status()
                self.root.after(1000, self.ai_move)
    
    def ai_move(self):
        if self.game_over or self.current_player != 'O':
            return
        
        best_score = -float('inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            self.board[best_move[0]][best_move[1]] = 'O'
            self.update_board_display()
            self.update_status()
            
            if not self.game_over:
                self.current_player = 'X'
                self.update_status()
    
    def minimax(self, is_maximizing):
        winner = self.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif self.is_full():
            return 0
        
        if is_maximizing:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        eval_score = self.minimax(False)
                        self.board[i][j] = ' '
                        max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        eval_score = self.minimax(True)
                        self.board[i][j] = ' '
                        min_eval = min(min_eval, eval_score)
            return min_eval
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    
    def update_board_display(self):
        button_font = font.Font(family="Helvetica", size=18, weight="bold")
        for i in range(3):
            for j in range(3):
                text = self.board[i][j]
                self.buttons[i][j].config(text=text, font=button_font)
                if text == 'X':
                    self.buttons[i][j].config(fg="blue", bg="#fff9c4")
                elif text == 'O':
                    self.buttons[i][j].config(fg="red", bg="#ffcccc")
                else:
                    self.buttons[i][j].config(fg="black", bg="#e0e0e0")
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
