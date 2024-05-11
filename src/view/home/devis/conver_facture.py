import tkinter as tk
from tkinter import messagebox
import json

from PIL import Image,ImageTk, ImageDraw
from tkinter import filedialog
import datetime


from const import *
from tools.event_entry import effacer_indicatif, effacer_Text_indicatif

from view.home.facture.infos_client import InfosClient
from view.home.facture.infos_entrprise import InfosEntreprise
from view.home.devis.table_convert import TableConvertArticle
from view.home.facture.prix_info_pay import InfosBancaire
from view.home.facture.singature import SignatureFrame


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
        self.info_facture()
        self.info_entrprise = InfosEntreprise(self.canv_fact,self.BDD, self.id_utilisateur)

        #on cherche des inofs de cleint apartir de son ref, defini dans encien facture 
        num_client = self.infos_devis[6]
        requet_cl = f"SELECT * FROM client WHERE num = '{num_client}' AND id_utilisateur = '{self.id_utilisateur}';"
        requet_cl = self.BDD.execute_requete(requet_cl)[0]
        self.info_client = InfosClient(self.canv_fact,requet_cl)

        table = json.loads(self.infos_devis[2])
        self.info_table_articles = TableConvertArticle(self.canv_fact,425, table )

        remarqu = self.infos_devis[4]


    def info_facture(self): 
        facture_label = tk.Label(self.canv_fact, text="FACTURE",bg=COULEUR_LABEL,font=(POLICE, 20,"bold"))
        self.canv_fact.create_window(500, 40, anchor="n", window=facture_label)
        # Num facture
        self.num_fact = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM facture;")[0][0])
        num_facture_label = tk.Label(self.canv_fact, text="Numbre facture : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(797, 70, anchor="n", window=num_facture_label)
        self.entry_num_fact = tk.Entry(self.canv_fact)
        self.canv_fact.create_window(925, 70, anchor="n", window=self.entry_num_fact)
        # Date facture
        date_facture_label = tk.Label(self.canv_fact, text="Date facture : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(805,100, anchor="n", window=date_facture_label)
        self.entry_date_fact = tk.Entry(self.canv_fact)
        self.canv_fact.create_window(925, 100, anchor="n", window=self.entry_date_fact)
        #Ref client 
        self.num_client = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM client;")[0][0])
        ref_cleint_label = tk.Label(self.canv_fact, text="Ref Client : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(810,130, anchor="n", window=ref_cleint_label)
        self.entry_ref_cleint = tk.Entry(self.canv_fact)
        self.canv_fact.create_window(925, 130, anchor="n", window=self.entry_ref_cleint)

        
        self.entry_num_fact.insert(0, f"FAC000{self.num_fact +1 }")
        self.entry_date_fact.insert(0,datetime.datetime.now().date()) #afficheer la date actule par defut
        self.entry_ref_cleint.insert(0,f"CL000{self.num_client + 1}") 
  

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
