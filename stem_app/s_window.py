import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        
        self.cards = [f"image{i}.png" for i in range(1, 9)]
        self.cards.extend(self.cards)
        random.shuffle(self.cards)
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None
        
        self.buttons = []
        
        for i in range(4):
            row = []
            for j in range(4):
                idx = i * 4 + j
                button = tk.Button(self.root, image=tk.PhotoImage(file="card_back.png"), command=lambda idx=idx: self.flip_card(idx))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
    
    def flip_card(self, idx):
        if self.flipped[idx] or self.num_flipped == 2:
            return
        
        self.flipped[idx] = True
        self.num_flipped += 1
        
        self.buttons[idx].config(image=tk.PhotoImage(file=self.cards[idx]))
        
        if self.num_flipped == 2:
            self.root.after(1000, self.check_match)
            self.prev_idx = idx
        else:
            self.prev_idx = idx
    
    def check_match(self):
        if self.cards[self.prev_idx] == self.cards[self.prev_idx]:
            self.buttons[self.prev_idx].config(state=tk.DISABLED)
            self.buttons[idx].config(state=tk.DISABLED)
        
        for i in range(16):
            if not self.flipped[i]:
                self.buttons[i].config(image=tk.PhotoImage(file="card_back.png"))
        
        self.flipped = [False] * 16
        self.num_flipped = 0
        self.prev_idx = None

def open_s_window():
    s_window = tk.Toplevel()
    s_window.title("Memory Game - S Window")
    
    game = MemoryGame(s_window)

    s_window.mainloop()

