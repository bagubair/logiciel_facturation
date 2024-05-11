import tkinter as tk
from tkinter import messagebox

from const import *
from tools.event_entry import effacer_indicatif

from view.home.devis.cree_devis import CreeDevis

class Devis():
    def __init__(self, root, frame_button, BDD, id_utilisateur):
        self.root = root
        self.frame_button = frame_button
        self.BDD = BDD
        self.id_utilisateur = id_utilisateur

        self.canvas = None
        self.root.after(10, self.initialisation)
        self.root.bind("<Configure>", self.on_configure)

        
    def initialisation(self):
        x = self.root.winfo_width()
        y = self.root.winfo_height()
        self.canvas = tk.Canvas(self.root, width=x, height=y,bg=COULEUR_PRINCIPALE)
        self.canvas.place(x=0, y=(65))



        self.recherhe_devis = tk.Entry(self.canvas,width=35,fg="gray")
        self.canvas.create_window(730, (y//26.66) , anchor="ne", window=self.recherhe_devis,tags="rech_devis")
        self.recherhe_devis.insert(0, "Recherche")


        devis = tk.Label(self.canvas, text="Num Devis",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(190, 73 , anchor="n", window=devis,tags="devis")
        client = tk.Label(self.canvas, text="Client",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(550, 73 , anchor="n", window=client,tags="client")
        montant = tk.Label(self.canvas, text="Montant Prévu",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(930, 73 , anchor="n", window=montant,tags="montant")

        # Création de la listebox
        self.listbox = tk.Listbox(self.canvas, selectmode=tk.SINGLE,  width=1090, height=500, font=(POLICE,10))
        self.canvas.create_window(600, 115, width=1090, height=500, anchor="n", window=self.listbox, tags="listbox")

        requet_devis = f"SELECT devis.num, client.nom, client.prenom, devis.montant FROM client, devis WHERE client.num = devis.ref_client AND devis.id_utilisateur = {self.id_utilisateur}"
        requet_devis  = self.BDD.execute_requete( requet_devis )
        
        for devis in requet_devis:
            nom_client = f"{ devis[1]} + {devis[2]}"
            format_info = f"{'':<15}{(devis[0] + (len(devis[0])%8)*" ")[0:8] :<18}{(nom_client + (len(nom_client)%25)*" ")[0:25]:<26}{(devis[2] + (len(devis[2])%10)*" ")[0:10]:>5}"
            self.listbox.insert(tk.END, format_info)



        self.ajoute = tk.Button(self.canvas, width=11, height=2,text="Creer Devis", command=lambda:self.ajoute_devis() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(300,660 , anchor="n", window=self.ajoute,tags="ajoute")
        
        self.modf = tk.Button(self.canvas, width=10, height=2,text="Modifier", command=lambda:self.modf_devis() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(430,660 , anchor="n", window=self.modf,tags="lire")

        self.convertir = tk.Button(self.canvas, width=18, height=2,text="Convertir en Facture", command=lambda:self.convertir_devis() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(590,660 , anchor="n", window=self.convertir,tags="convertir")
        
        self.supprim = tk.Button(self.canvas, width=10, height=2,text="Supprimer", command=lambda:self.supprim_devis() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(770,660 , anchor="n", window=self.supprim,tags="supr")

    
    def ajoute_devis(self):
        self.canvas.destroy()
        CreeDevis(self.root,self.frame_button,self.BDD, self.id_utilisateur) #defini dans  (cree_devis.py)

    def modf_devis(self):
        indice_devis = self.listbox.curselection()
        if indice_devis:
            format_box =self.listbox.get(indice_devis)
            num_devis = format_box.split()[0]
            requet_devis = f"SELECT * FROM devis WHERE num = '{num_devis}' AND id_utilisateur = '{self.id_utilisateur}';"
            requet_devis = self.BDD.execute_requete(requet_devis)[0]
            print(requet_devis)
            self.canvas.destroy()
            CreeDevis(self.root,self.frame_button,self.BDD, self.id_utilisateur,requet_devis) #defini dans  (cree_devis.py)

        else:
            messagebox.showerror("Erreur", "Vous devez sélectionner une facture.")




    def on_configure(self, event):
        if (self.canvas):
            # Recalculer les dimensions de la fenêtre
            long = self.root.winfo_width()
            haut = self.root.winfo_height()
            self.frame_button.config(width=long, height=(haut // 11.42))
            self.frame_button.place(x=0, y=0)

            self.canvas.config(width=long, height=haut)
            self.canvas.place(x=0, y=(haut // 11.42))
