import os
import tkinter as tk

#from PIL import Image, ImageTk
from const import *
#from .tools.image_size import size_photo
#from view.home.aide import Aide
#from view.home.quit_button import Quitter

"""
La classe BackGroundMain initialise la page principale du jeu (première page),
qui va contenir les boutons 'Quitter' et 'Aide'et afficher le nom du jeu 'EN GARDE'.
"""
class Home:
    def __init__(self, root):
        self.root = root

        self.root.after(10, self.initialisation)
        self.root.bind("<Configure>", self.on_configure)


    def initialisation(self):
        long = self.root.winfo_width()
        haut = self.root.winfo_height()
        self.list_button = []
        self.frame_button = tk.Frame(self.root, width=long, height=(haut // 11.42), bg=COULEUR_BOUTON)
        self.frame_button.grid_propagate(False)  # Empêcher le frame de redimensionner ses cellules
        self.frame_button.place(x=0, y=0)
        for i in range(5) :
            button = tk.Button(self.frame_button, width=20, height=3,bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON, font=(POLICE, 10,"bold"),anchor="center")
            if(i==0):
                button.grid(row=0, column=i,padx=(190,5), pady=(6,4), sticky="w")
            else:
                button.grid(row=0, column=i,padx=(5,5), pady=(6,4), sticky="w")
            self.list_button.append(button)
        #preciser les noms et commandes des button
        self.list_button[0].config(text="Facture", command=lambda:self.facture() )
        self.list_button[1].config(text="Devis", command=lambda: self.devis())
        self.list_button[2].config(text="Articles", command=lambda:self.article())
        self.list_button[3].config(text="Clients", command=lambda: self.client())
        self.list_button[4].config(text="Paramètres", command=lambda: self.parametre())

        self.button_active =0
        # Créer un Canvas
        self.canvas_home = tk.Canvas(self.root, width=long, height=haut,bg=COULEUR_PRINCIPALE)
        self.canvas_home.place(x=0, y=(haut // 11.42))
        #root.grid_rowconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en hauteur
        #root.grid_columnconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en largeur

        


    def facture(self):
        """on change le couluer de button active juste pour montrer que c'est lui activé """
        self.list_button[self.button_active].config(bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.list_button[0].config(bg=COULEUR_TEXT_BOUTON,fg=COULEUR_BOUTON)
        self.button_active = 0
        

    def devis(self):
        """on change le couluer de button active juste pour montrer que c'est lui activé """
        self.list_button[self.button_active].config(bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.list_button[1].config(bg=COULEUR_TEXT_BOUTON,fg=COULEUR_BOUTON)
        self.button_active = 1
        

    def article(self):
        """on change le couluer de button active juste pour montrer que c'est lui activé """
        self.list_button[self.button_active].config(bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.list_button[2].config(bg=COULEUR_TEXT_BOUTON,fg=COULEUR_BOUTON)
        self.button_active = 2
        
    def client(self):
        """on change le couluer de button active juste pour montrer que c'est lui activé """
        self.list_button[self.button_active].config(bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.list_button[3].config(bg=COULEUR_TEXT_BOUTON,fg=COULEUR_BOUTON)
        self.button_active = 3
        

    def parametre(self):
        """on change le couluer de button active juste pour montrer que c'est lui activé """
        self.list_button[self.button_active].config(bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.list_button[4].config(bg=COULEUR_TEXT_BOUTON,fg=COULEUR_BOUTON)
        self.button_active = 4
        

    def on_configure(self, event):
        if (self.canvas_home) and (self.frame_button):
            # Recalculer les dimensions de la fenêtre
            long = self.root.winfo_width()
            haut = self.root.winfo_height()

            self.frame_button.config(width=long, height=(haut // 11.42))
            self.frame_button.place(x=0, y=0)
            self.canvas_home.config(width=long, height=haut)
            self.canvas_home.place(x=0, y=(haut // 11.42))
           