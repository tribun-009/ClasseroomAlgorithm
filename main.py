import tkinter as tk
from Emploi_du_temps.EmploiDuTemps import EmploiDuTemps

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.edt = EmploiDuTemps()

    def window(self):
        self.root.title("Emploi du temps")
        self.root.geometry("700x400")
        self.root.mainloop()

    def afficher_jours(self):
        jours = self.edt.jours

        for jour in jours:
            label = tk.Label(self.root, text=jour, font=("Arial", 16))
            label.pack(side="left", padx=10)

if __name__ == "__main__":
    window = MainWindow()
    window.afficher_jours()
    window.window()

