import tkinter as tk
import random
from tkinter import messagebox
from math import sqrt

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Area Calculator")
        
        self.label_info = tk.Label(self.root, text="Select a sublevel:")
        self.label_info.pack(pady=10)
        
        self.sublevels = [
            {"text": "Calculate Area", "function": self.open_area_sublevel},
            {"text": "Calculate Cathetus (Pythagorean Theorem)", "function": self.open_cathetus_sublevel},
            {"text": "Calculate Perimeter", "function": self.open_perimeter_sublevel}
        ]
        
        for sublevel in self.sublevels:
            button = tk.Button(self.root, text=sublevel["text"], command=sublevel["function"])
            button.pack()
    
def open_area_sublevel():
    root = tk.Tk()
    root.title("Calculate Triangle Area")
    
    canvas = tk.Canvas(root, width=200, height=150)
    canvas.pack(pady=10)
    
    base = random.randint(5, 15)
    height = random.randint(5, 15)
    
    canvas.create_polygon(50, 150, 150, 150, 100, 150 - height, fill="lightblue")
    
    label_base = tk.Label(root, text=f"Base: {base}")
    label_base.pack()
    
    label_height = tk.Label(root, text=f"Height: {height}")
    label_height.pack()
    
    entry_area = tk.Entry(root)
    entry_area.pack(pady=10)
    
    calculate_button = tk.Button(root, text="Calculate Area", command=lambda: calculate_area(entry_area, base, height))
    calculate_button.pack()
    
    result_label = tk.Label(root, text="")
    result_label.pack()
    
    root.mainloop()

    
    def open_cathetus_sublevel(self):
        self.root.destroy()  # Close current window
        open_cathetus_window()
    
    def open_perimeter_sublevel(self):
        self.root.destroy()  # Close current window
        open_perimeter_window()

def open_m_window():
    m_window = tk.Toplevel()
    m_window.title("Triangle Sublevels - T Window")
    
    calculator = AreaCalculator(m_window)

    m_window.mainloop()
