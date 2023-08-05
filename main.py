import tkinter as tk
from stem_app.s_window import open_s_window
from stem_app.t_window import open_t_window
from stem_app.e_window import open_e_window
from stem_app.m_window import open_m_window

class STEMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("STEM App")
        
        self.canvas = tk.Canvas(self.root, width=800, height=300)
        self.canvas.pack()

        self.circle_s = self.canvas.create_oval(100, 100, 200, 200, fill="blue")
        self.circle_t = self.canvas.create_oval(250, 100, 350, 200, fill="green")
        self.circle_e = self.canvas.create_oval(400, 100, 500, 200, fill="orange")
        self.circle_m = self.canvas.create_oval(550, 100, 650, 200, fill="red")
        
        self.canvas.create_line(200, 150, 250, 150, fill="black")
        self.canvas.create_line(350, 150, 400, 150, fill="black")
        self.canvas.create_line(500, 150, 550, 150, fill="black")
        
        self.canvas.create_text(150, 150, text="S", font=("Helvetica", 24))
        self.canvas.create_text(300, 150, text="T", font=("Helvetica", 24))
        self.canvas.create_text(450, 150, text="E", font=("Helvetica", 24))
        self.canvas.create_text(600, 150, text="M", font=("Helvetica", 24))
        
        self.canvas.tag_bind(self.circle_s, '<Button-1>', self.open_s)
        self.canvas.tag_bind(self.circle_t, '<Button-1>', self.open_t)
        self.canvas.tag_bind(self.circle_e, '<Button-1>', self.open_e)
        self.canvas.tag_bind(self.circle_m, '<Button-1>', self.open_m)
    
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
