import tkinter as tk
import random
from tkinter import messagebox
from math import sqrt

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculador d'àrea de triangles")
        
        self.label_info = tk.Label(self.root, text="Selecciona un subnivell:")
        self.label_info.pack(pady=10)
        
        self.sublevels = [
            {"text": "Calcular àrea", "function": self.open_area_sublevel},
            {"text": "Calcular Catets (Pitàgores)", "function": self.open_cathetus_sublevel},
            {"text": "Calcular Perímetre", "function": self.open_perimeter_sublevel}
        ]
        
        for sublevel in self.sublevels:
            button = tk.Button(self.root, text=sublevel["text"], command=sublevel["function"])
            button.pack()
    
    def open_area_sublevel(self):
        self.root.destroy()  # Close current window
        open_area_window()
    
    def open_cathetus_sublevel(self):
        self.root.destroy()  # Close current window
        open_cathetus_window()
    
    def open_perimeter_sublevel(self):
        self.root.destroy()  # Close current window
        open_perimeter_window()

def open_area_window():
    area_window = tk.Toplevel()
    area_window.title("Calcular l'àrea d'un triangle")
    
    canvas = tk.Canvas(area_window, width=400, height=300)  # Increase canvas size
    canvas.pack(pady=10)
    
    base = random.randint(5, 15)
    height = random.randint(5, 15)
    
    # Scale the triangle's dimensions to fit canvas size
    scale_factor = 10
    triangle_coords = [
        200 - base * scale_factor / 2, 300,
        200 + base * scale_factor / 2, 300,
        200, 300 - height * scale_factor,
    ]
    canvas.create_polygon(triangle_coords, fill="red")
    
    label_base = tk.Label(area_window, text=f"Base: {base}")
    label_base.pack()
    
    label_height = tk.Label(area_window, text=f"Altura: {height}")
    label_height.pack()
    
    entry_area = tk.Entry(area_window)
    entry_area.pack(pady=10)
    
    attempts_left = 3
    result_label = tk.Label(area_window, text=f"Intents restants: {attempts_left}")
    result_label.pack()

    def calculate_area():
        nonlocal attempts_left
        
        try:
            user_area = float(entry_area.get())
            correct_area = 0.5 * base * height
            
            if user_area == correct_area:
                result = "Correcte! Molt bé!"
                area_window.destroy()  # Close window on correct answer
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    result = f"Incorrecte:(). Torna-ho a intentar. Intents restants: {attempts_left}"
                else:
                    result = f"Incorrecte. La resposta correcte de l'àrea és {correct_area}. Clica OK per continuar."
                    entry_area.config(state="disabled")  # Disable entry after 3 attempts
                    ok_button.config(state="normal")  # Enable OK button
                
            result_label.config(text=result)
            entry_area.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Siusplau, introdueix un número vàlid.")

    calculate_button = tk.Button(area_window, text="Calculate Area", command=calculate_area)
    calculate_button.pack()

    ok_button = tk.Button(area_window, text="OK", state="disabled", command=area_window.destroy)
    ok_button.pack()

def open_cathetus_window():
    # Define the function for opening the cathetus window
    pass

def open_perimeter_window():
    # Define the function for opening the perimeter window
    pass

def open_t_window():
    t_window = tk.Toplevel()
    t_window.title("Triangle Sublevels - T Window")
    
    calculator = AreaCalculator(t_window)

    t_window.mainloop()


