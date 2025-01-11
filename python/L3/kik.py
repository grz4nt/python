import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kółko i krzyżyk 5x5")
        self.window.geometry("480x600")
        
        self.current_player = "X"
        self.board = [['' for _ in range(5)] for _ in range(5)]
        
        self.buttons = []
        for i in range(5):
            row = []
            for j in range(5):
                button = tk.Button(
                    self.window,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.ruch(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)
        
        self.player_label = tk.Label(
            self.window,
            text=f"Ruch gracza: {self.current_player}",
            font=('Arial', 14)
        )
        self.player_label.grid(row=5, column=0, columnspan=5, pady=10)
        
        reset_button = tk.Button(
            self.window,
            text="Nowa gra",
            font=('Arial', 12),
            command=self.reset
        )
        reset_button.grid(row=6, column=0, columnspan=5)

    def ruch(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.wygrana(row, col):
                messagebox.showinfo("Koniec gry", f"Gracz {self.current_player} wygrywa")
                self.reset()
            elif self.remis():
                messagebox.showinfo("Koniec gry", "Remis")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_label.config(text=f"Ruch gracza: {self.current_player}")

    def wygrana(self, row, col):
        for c in range(max(0, col-2), min(5, col+1)):
            if c+2 < 5:
                if self.board[row][c] == self.current_player and \
                   self.board[row][c+1] == self.current_player and \
                   self.board[row][c+2] == self.current_player:
                    return True
        
        for r in range(max(0, row-2), min(5, row+1)):
            if r+2 < 5:
                if self.board[r][col] == self.current_player and \
                   self.board[r+1][col] == self.current_player and \
                   self.board[r+2][col] == self.current_player:
                    return True

        for i in range(-2, 1):
            if 0 <= row+i <= 2 and 0 <= col+i <= 2:
                if row+i+2 < 5 and col+i+2 < 5:
                    if self.board[row+i][col+i] == self.current_player and \
                       self.board[row+i+1][col+i+1] == self.current_player and \
                       self.board[row+i+2][col+i+2] == self.current_player:
                        return True

        for i in range(-2, 1):
            if 0 <= row+i <= 2 and 0 <= col-i <= 4:
                if row+i+2 < 5 and col-i-2 >= 0:
                    if self.board[row+i][col-i] == self.current_player and \
                       self.board[row+i+1][col-i-1] == self.current_player and \
                       self.board[row+i+2][col-i-2] == self.current_player:
                        return True

        return False

    def remis(self):
        return all(self.board[i][j] != "" for i in range(5) for j in range(5))

    def reset(self):
        self.current_player = "X"
        self.board = [['' for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.buttons[i][j].config(text="")
        self.player_label.config(text=f"Ruch gracza: {self.current_player}")

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()