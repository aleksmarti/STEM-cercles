import tkinter as tk
from tkinter import messagebox

from stem_app.s_window import open_s_window
from stem_app.t_window import open_t_window
from stem_app.e_window import open_e_window
from stem_app.m_window import open_m_window

class STEMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("STEM PREPARADES App")
        
        self.canvas = tk.Canvas(self.root, width=1000, height=500)
        self.canvas.pack()

        self.circle_s = self.canvas.create_oval(100, 100, 200, 200, fill="blue")
        self.circle_t = self.canvas.create_oval(250, 100, 350, 200, fill="green")
        self.circle_e = self.canvas.create_oval(400, 100, 500, 200, fill="orange")
        self.circle_m = self.canvas.create_oval(550, 100, 650, 200, fill="red")
        
        self.canvas.create_line(200, 150, 250, 150, fill="black")
        self.canvas.create_line(350, 150, 400, 150, fill="black")
        self.canvas.create_line(500, 150, 550, 150, fill="black")
        
        self.canvas.create_text(150, 150, text="S", font=("Arial", 24))
        self.canvas.create_text(300, 150, text="T", font=("Arial", 24))
        self.canvas.create_text(450, 150, text="E", font=("Arial", 24))
        self.canvas.create_text(600, 150, text="M", font=("Arial", 24))
        
        self.canvas.tag_bind(self.circle_s, '<Button-1>', self.open_s)
        self.canvas.tag_bind(self.circle_t, '<Button-1>', self.open_t)
        self.canvas.tag_bind(self.circle_e, '<Button-1>', self.open_e)
        self.canvas.tag_bind(self.circle_m, '<Button-1>', self.open_m)
        
        # Carregar y mostrar la imatge de la dona
        self.woman_photo = tk.PhotoImage(file="woman.png")  # Canviar "woman.png" por la meva imatge
        
        self.woman_label = tk.Label(self.root, image=self.woman_photo)
        self.woman_label.image = self.woman_photo  # Mantenir referència per evitar eliminació
        self.woman_label.place(x=370, y=220)

        # Bafarada del diàleg
        self.dialog_label = tk.Label(self.root, text="Benvinguts al joc,nosaltres som dones STEM, selecciona uns dels nivells", bg="white")
        self.dialog_label.place(x=450, y=400)
        self.dialog_visible = False
        
    
        
    def open_s(self, event):
        open_s_window()
    
    def open_t(self, event):
        open_t_window()
    
    def open_e(self, event):
        open_e_window()
    
    def open_m(self, event):
        open_m_window()

        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = STEMApp(root)
    app.run()
