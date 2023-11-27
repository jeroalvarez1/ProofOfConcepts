import tkinter as tk

class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Merger 0.1")

        self.menubar = tk.Menu(self.root)

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="CSV Merger", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Correr', font=('Arial', 18))
        self.button.pack()

        self.root.mainloop()

MainMenu()