import os
import tkinter as tk
from consts import COULEUR_PRINCIPALE, COULEUR_TEXT_BOUTON, COULEUR_BOUTON, DATA_DIR 
"""
la class aide fait un button menu pour que le joueur choisit les regles qu'il veux pour la niveux de jeu 
la fonction ( FctOuvrir ) permet d'ouvrir le ficher dans un top level 
"""

class Aide:
    def __init__(self, canvas):
        # ------------------------------------------------------------------------------------
        self.aide = tk.Menubutton(canvas, text="Aide", relief="raised",bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON,
                    font=("Palatino Linotype", 12))
        self.aide.place(relx=0.96, rely=0.09, anchor="center")
        #self.menu1 = tk.Menu(self.aide, tearoff=False ,bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        #self.menu1.add_command(label="Regle Base",
                               #command=lambda: self.FctOuvrir(os.path.join(DATA_DIR, "regle_base.txt")))
        #self.menu1.add_command(label="Regle Clasique",
                               #command=lambda: self.FctOuvrir(os.path.join(DATA_DIR, "regle_clasique.txt")))
        #self.menu1.add_command(label="Regle Avancer",
                               #command=lambda: self.FctOuvrir(os.path.join(DATA_DIR, "regle_avancer.txt")))
        #self.aide.config(menu=self.menu1)

    def FctOuvrir(self, fichier):
        # Créer une nouvelle fenêtre Toplevel
        new_wind = tk.Toplevel()
        new_wind.geometry("1000x800")
        new_wind["bg"] = COULEUR_PRINCIPALE
        new_wind.title("Regle du jeu")
        # Créer un nouveau canvas dans la  fenêtre aide
        new_canvas = tk.Canvas(new_wind, width=1000, height=800, bg=COULEUR_PRINCIPALE)
        #self.scrol_aid = tk.Scrollbar(new_wind, command=new_canvas.yview, orient="vertical", bg=COULEUR_BOUTON)
        #self.scrol_aid.pack(side="right", fill="y")
        #new_canvas.configure(yscrollcommand=self.scrol_aid.set , scrollregion=new_canvas.bbox("all"))
  
        new_canvas.pack()

        with open(fichier, 'r') as file:
            texte = file.read()
            new_canvas.create_text(10, 10, text=texte, anchor='nw' , font=("Palatino Linotype", 9))

        # Ajouter un bouton pour détruire la nouvelle fenêtre
        new_but = tk.Button(new_canvas, text="Fermer", command=new_wind.destroy ,font=("Palatino Linotype", 12),
                             bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        new_but.place(relx=0.91, rely=0.95, anchor="center")
