import tkinter as tk

def open_e_window():
    e_window = tk.Toplevel()
    e_window.title("E Window")
    
    label = tk.Label(e_window, text="This is the E window.")
    label.pack()
