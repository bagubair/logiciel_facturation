#app.py
import tkinter as tk
import psycopg2 as sql

from const import *
from view.login_page.connection import Connection
from model.basse_donnes import BaseDeDonnee


class RootPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{LONGUEUR}x{HAUTEUR}")
        self.root["bg"] = COULEUR_PRINCIPALE
        self.root.option_add('*font', (POLICE, 8,"bold"))
        self.root.minsize(LONGUEUR, HAUTEUR)
        self.root.title("Facturation")
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        
        self.basse_BDD = BaseDeDonnee("factur", "emad_70", "439155")
        self.basse_BDD.init_table()

        self.connec = Connection(self.root,self.basse_BDD)
        self.login_screen()

        

    def login_screen(self):
        self.connec.main_connec()
        
        

    def mainloop(self):
        self.root.mainloop()



def Demarer():
    app = RootPrincipal()
    app.mainloop()


if __name__ == "__main__":
    Demarer()
