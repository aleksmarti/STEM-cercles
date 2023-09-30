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
        self.root.destroy()  # Tanca la finestra actual
        open_area_window()
    
    def open_cathetus_sublevel(self):
        self.root.destroy()  # Tanca la finestra actual
        open_cathetus_window()
    
    def open_perimeter_sublevel(self):
        self.root.destroy()  # Tanca la finestra actual
        open_perimeter_window()

def open_area_window():
    area_window = tk.Toplevel()
    area_window.title("Calcular l'àrea d'un triangle")
    
    canvas = tk.Canvas(area_window, width=400, height=300)  # Amplia la mida 
    canvas.pack(pady=10)
    
    base = random.randint(5, 15)
    height = random.randint(5, 15)
    
    # escala les dimensions del triangle per adaptar-se a la mida 
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
                area_window.destroy()  # Tanca la finestra quan la resposta sigui correcta
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    result = f"Incorrecte:(). Torna-ho a intentar. Intents restants: {attempts_left}"
                else:
                    result = f"Incorrecte. La resposta correcte de l'àrea és {correct_area}. Clica OK per continuar."
                    entry_area.config(state="disabled")  # Desactiva l'entrada després de 3 intents
                    ok_button.config(state="normal")  # Activa el botó d'acord
                
            result_label.config(text=result)
            entry_area.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Siusplau, introdueix un número vàlid.")

    calculate_button = tk.Button(area_window, text="Calcular Àrea", command=calculate_area)
    calculate_button.pack()

    ok_button = tk.Button(area_window, text="OK", state="disabled", command=area_window.destroy)
    ok_button.pack()

def open_cathetus_window():
    # Funció per obrir la finestra de càlcul dels catets

    def calculate_cathetus():
        try:
            side_a = float(entry_side_a.get())
            side_b = float(entry_side_b.get())

            hypotenuse = sqrt(side_a**2 + side_b**2)
            
            result_label.config(text=f"La hipotenusa és: {hypotenuse:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Siusplau, introdueix valors vàlids per els catets.")

    cathetus_window = tk.Toplevel()
    cathetus_window.title("Calcular Catets (Pitàgores)")

    label_side_a = tk.Label(cathetus_window, text="Introdueix la longitud del catet A:")
    label_side_a.pack()

    entry_side_a = tk.Entry(cathetus_window)
    entry_side_a.pack(pady=10)

    label_side_b = tk.Label(cathetus_window, text="Introdueix la longitud del catet B:")
    label_side_b.pack()

    entry_side_b = tk.Entry(cathetus_window)
    entry_side_b.pack(pady=10)

    calculate_button = tk.Button(cathetus_window, text="Calcular", command=calculate_cathetus)
    calculate_button.pack()

    result_label = tk.Label(cathetus_window, text="")
    result_label.pack()

def open_perimeter_window():
    # Funció per obrir la finestra de càlcul del perímetre

    def calculate_perimeter():
        try:
            side_a = float(entry_side_a.get())
            side_b = float(entry_side_b.get())
            side_c = float(entry_side_c.get())

            perimeter = side_a + side_b + side_c
            
            result_label.config(text=f"El perímetre és: {perimeter:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Siusplau, introdueix valors vàlids per les longituds dels costats.")

    perimeter_window = tk.Toplevel()
    perimeter_window.title("Calcular el Perímetre d'un triangle")

    label_side_a = tk.Label(perimeter_window, text="Introdueix la longitud del costat A:")
    label_side_a.pack()

    entry_side_a = tk.Entry(perimeter_window)
    entry_side_a.pack(pady=10)

    label_side_b = tk.Label(perimeter_window, text="Introdueix la longitud del costat B:")
    label_side_b.pack()

    entry_side_b = tk.Entry(perimeter_window)
    entry_side_b.pack(pady=10)

    label_side_c = tk.Label(perimeter_window, text="Introdueix la longitud del costat C:")
    label_side_c.pack()

    entry_side_c = tk.Entry(perimeter_window)
    entry_side_c.pack(pady=10)

    calculate_button = tk.Button(perimeter_window, text="Calcular", command=calculate_perimeter)
    calculate_button.pack()

    result_label = tk.Label(perimeter_window, text="")
    result_label.pack()


def open_m_window():
    m_window = tk.Toplevel()
    m_window.title("Triangle Sublevels - T Window")
    
    calculator = AreaCalculator(m_window)

    m_window.mainloop()
   