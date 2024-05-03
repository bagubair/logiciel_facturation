import tkinter as tk
import os


from const import *



def effacer_indicatif(entry_widget, indicatif):
    """on efface le text d'indication et remplace par le text entrée par utilisateur"""
    if entry_widget.get() == indicatif:
        entry_widget.delete(0, tk.END)
        entry_widget.config(fg=COULEUR_BOUTON)  # Changer la couleur du texte entré par l'utilisateur



def reste_indicatif(entry_widget, indicatif):
    """si l'utilsateur rein entrée on garde le text indicatif"""
    if not entry_widget.get():
        entry_widget.insert(0, indicatif)
        entry_widget.config(fg="gray")  # Revenir à la couleur du texte indicatif
