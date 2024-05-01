import os
import tkinter as tk

from PIL import Image, ImageTk
from const import LONGUEUR, HAUTEUR, DATA_DIR , COULEUR_TEXT_BOUTON , COULEUR_BOUTON
from .tools.image_size import size_photo
from view.home.aide import Aide
#from view.home.quit_button import Quitter

"""
La classe BackGroundMain initialise la page principale du jeu (première page),
qui va contenir les boutons 'Quitter' et 'Aide'et afficher le nom du jeu 'EN GARDE'.
"""
class BackGroundMain:
    def __init__(self, root):
        # Créer un Canvas
        self.canvas = tk.Canvas(root, width=LONGUEUR, height=HAUTEUR)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        root.grid_rowconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en hauteur
        root.grid_columnconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en largeur

        # Charger et redimensionner l'image initiale
        #self.background_image = size_photo(os.path.join(DATA_DIR, "screen_1.jpg"), LONGUEUR, HAUTEUR)
        # Ajouter l'image au canvas
        #self.image_item = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Ajouter le texte au centre du canvas
        texte_centre_x = LONGUEUR // 2
        texte_centre_y = HAUTEUR // 2
        #self.canvas.create_text(935, 630, text="EN GARDE", font=("Arial", 45, "bold"), fill="#00ff00") # #00ff00 : coulour green

        # Lier la fonction de redimensionnement à l'événement de changement de taille du canvas
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        self.aide = Aide(self.canvas)
        #self.quit = Quitter(self.canvas)

    # Récupérer la nouvelle taille du canvas
    def on_canvas_resize(self, event):
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()

        # Redimensionner l'image pour s'adapter à la nouvelle taille
        self.photo = size_photo(os.path.join(DATA_DIR, "screen_1.jpg"), new_width, new_height)
        # Mettre à jour l'image sur le canvas
        self.canvas.itemconfig(self.image_item, image=self.photo)
