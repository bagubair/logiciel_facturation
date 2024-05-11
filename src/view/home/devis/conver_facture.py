import tkinter as tk
from tkinter import messagebox
import json

from PIL import Image,ImageTk, ImageDraw
from tkinter import filedialog
import datetime


from const import *
from tools.event_entry import effacer_indicatif, effacer_Text_indicatif


class ConverDevis():
    def __init__(self, root,frame_button,BDD, id_utilisateur, infos_devis):
        self.root = root
        self.frame_button = frame_button
        self.BDD = BDD
        self.id_utilisateur = id_utilisateur
        self.infos_devis = infos_devis
        
        self.root.after(10, self.initialisation)
        self.root.bind("<Configure>", self.on_configure)

    def initialisation(self):

        self.x = self.root.winfo_width()
        self.y = self.root.winfo_height()

        self.canvas = tk.Canvas(self.root, width=self.x, height=self.y,bg=COULEUR_PRINCIPALE)
        self.canvas.place(x=0, y=(self.y //11.42))

        self.frame_fact = tk.Frame(self.canvas, width=(self.x//1.2), height=(self.y//1.176), bg=COULEUR_LABEL)
        self.frame_fact.grid_propagate(False)  # Empêcher le frame de redimensionner ses cellules
        self.frame_fact.place(x=100, y=0)

        # Création du canevas avec la barre de défilement
        self.canv_fact = tk.Canvas(self.frame_fact,width=(self.x//1.2), height=(self.y//1.176), yscrollincrement=8, bg=COULEUR_LABEL)
        self.canv_fact.grid_propagate(False)
        self.scrol_fact = tk.Scrollbar(self.frame_fact, command=self.canv_fact.yview, orient="vertical", bg=COULEUR_PRINCIPALE)
        self.scrol_fact.pack(side="right", fill="y")
        self.canv_fact.configure(yscrollcommand=self.scrol_fact.set)
        self.canv_fact.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  # Remplir le canevas avec tout l'espace disponible

        self.cree_facture()



    def cree_facture(self):
        pass

    def on_configure(self, event):
        if (self.canvas):
            # Recalculer les dimensions de la fenêtre
            x = self.root.winfo_width()
            y = self.root.winfo_height()

            self.frame_button.config(width=x, height=(y // 11.42))
            self.frame_button.place(x=0, y=0)

            self.canvas.config(width=x, height=y)
            self.canvas.place(x=0, y=(y //11.42))

            self.frame_fact.config(width=1000, height=(y//1.176))
            self.frame_fact.place(x=(x-1000)//2, y=10)
            self.canv_fact.config(width=1000,height=(y//1.176))
