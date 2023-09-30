"""import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Joc de preguntes")
        
        self.questions = [
            {
                "question": "Quina d'aquestes professions no pertany a STEM?",
                "options": ["A. Literatura", "B. Astrofísica", "C. Robòtica"],
                "correct_answer": "A"
            },
            {
                "question": "Quina científica va determinar l'estructura de l'ADN?",
                "options": ["A. Barbara McClintock", "B. Barbara Walters", "C. Rosalind Franklin"],
                "correct_answer": "C"
            },
            {
                "question": "Quina dona va inventar el Wi-fi?",
                "options": ["A. Hedy Lamarr", "B. Sally Ride", "C. Mae Jemison"],
                "correct_answer": "A"
            },
            {
                "question": "Quina d'aquestes dones ens va ajudar a arribar a la Lluna?",
                "options": ["A. Margaret Hamilton", "B. Ada Lovelace", "C. Cèlia Garcia"],
                "correct_answer": "A"

                "question": "Quina d'aquestes professions no pertany a STEM?",
                "options": ["A. Enginyeria", "B. Comunicacions", "C. Microbiologia"],
                "correct_answer": "B"
            }
        ]
        
        self.current_question = 0
        self.score = 0 # Puntació inicial és 0
        
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.display_question()
    
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            
            for i in range(3):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_score()
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if correct_answer == chr(ord("A") + selected_option):
            self.score += 1
        
        self.current_question += 1
        self.display_question()
    
    def show_score(self):
        self.question_label.config(text=f"La teva puntuació és: {self.score} de {len(self.questions)}")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

def open_t_window():
    t_window = tk.Toplevel()
    t_window.title("T Window")
    
    quiz = QuizGame(t_window)
"""
import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Joc de preguntes")
        
        self.questions = [
            {
                "question": "Quina d'aquestes professions no pertany a STEM?",
                "options": ["A. Literatura", "B. Astrofísica", "C. Robòtica"],
                "correct_answer": "A"
            },
            {
                "question": "Quina científica va determinar l'estructura de l'ADN?",
                "options": ["A. Barbara McClintock", "B. Barbara Walters", "C. Rosalind Franklin"],
                "correct_answer": "C"
            },
            {
                "question": "Quina dona va inventar el Wi-fi?",
                "options": ["A. Hedy Lamarr", "B. Sally Ride", "C. Mae Jemison"],
                "correct_answer": "A"
            },
            {
                "question": "Quina d'aquestes dones ens va ajudar a arribar a la Lluna?",
                "options": ["A. Margaret Hamilton", "B. Ada Lovelace", "C. Cèlia Garcia"],
                "correct_answer": "A"
            }
        ]
        import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Joc de preguntes")
        
        self.questions = [
            {
                "question": "Quina d'aquestes professions no pertany a STEM?",
                "options": ["A. Literatura", "B. Astrofísica", "C. Robòtica"],
                "correct_answer": "A"
            },
            {
                "question": "Quina científica va determinar l'estructura de l'ADN?",
                "options": ["A. Barbara McClintock", "B. Barbara Walters", "C. Rosalind Franklin"],
                "correct_answer": "C"
            },
            {
                "question": "Quina dona va inventar el Wi-fi?",
                "options": ["A. Hedy Lamarr", "B. Sally Ride", "C. Mae Jemison"],
                "correct_answer": "A"
            },
            {
                "question": "Quina d'aquestes dones ens va ajudar a arribar a la Lluna?",
                "options": ["A. Margaret Hamilton", "B. Ada Lovelace", "C. Cèlia Garcia"],
                "correct_answer": "A"
            }
        ]
        
        self.current_question = -1
        self.score = 0
        
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.score_label = tk.Label(self.root, text="")
        self.score_label.pack()

        # Agregamos una etiqueta para mostrar la puntuación final
        self.final_score_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.final_score_label.pack()

        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            
            for i in range(3):
                self.option_buttons[i].config(text=question_data["options"][i], state=tk.NORMAL)
            
            self.score_label.config(text="Puntuació: " + str(self.score))
        else:
            self.show_final_score()
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if correct_answer == chr(ord("A") + selected_option):
            self.score += 1

        self.score_label.config(text="Resposta correcta: " + correct_answer)
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

        self.root.after(2000, self.next_question)
    
    def show_final_score(self):
        self.question_label.config(text="")
        self.score_label.config(text="")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

        # Calculamos la puntuación final sobre el total de preguntas
        final_score = f"Puntuació final: {self.score} de {len(self.questions)}"
        self.final_score_label.config(text=final_score)

def open_t_window():
    t_window = tk.Toplevel()
    t_window.title("T Window")
    
    quiz = QuizGame(t_window)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Joc de preguntes")
    open_t_window()
    root.mainloop()


