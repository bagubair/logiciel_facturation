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
from view.home.facture.singature import SignatureFrame
from view.home.devis.table_articles_devis import TableArticleDevis


class CreeDevis():
    def __init__(self, root,frame_button,BDD, id_utilisateur, encien_devis=None):
        self.root = root
        self.frame_button = frame_button
        self.BDD = BDD
        self.id_utilisateur = id_utilisateur
        self.encien_devis = encien_devis #dans cas juste modifier une devis 
        
        self.root.after(10, self.initialisation)
        self.root.bind("<Configure>", self.on_config)

    def initialisation(self):

        self.x = self.root.winfo_width()
        self.y = self.root.winfo_height()

        self.canvas = tk.Canvas(self.root, width=self.x, height=self.y,bg=COULEUR_PRINCIPALE)
        self.canvas.place(x=0, y=(self.y //11.42))

        self.frame_devis = tk.Frame(self.canvas, width=(self.x//1.2), height=(self.y//1.176), bg=COULEUR_LABEL)
        self.frame_devis.grid_propagate(False)  # Empêcher le frame de redimensionner ses cellules
        self.frame_devis.place(x=100, y=0)

        # Création du canevas avec la barre de défilement
        self.canv_devis = tk.Canvas(self.frame_devis,width=(self.x//1.2), height=(self.y//1.176), yscrollincrement=8, bg=COULEUR_LABEL)
        self.canv_devis.grid_propagate(False)
        self.scrol_devis = tk.Scrollbar(self.frame_devis, command=self.canv_devis.yview, orient="vertical", bg=COULEUR_PRINCIPALE)
        self.scrol_devis.pack(side="right", fill="y")
        self.canv_devis.config(yscrollcommand=self.scrol_devis.set)
        self.canv_devis.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  # Remplir le canevas avec tout l'espace disponible
       
        self.cree_devis()

        bouton_annule = tk.Button(self.canvas, text="Annuler",height=1,bg=COULEUR_CANVAS,font=(POLICE, 11,"bold"), command=lambda: self.annule())
        self.canvas.create_window(470, 863, anchor="n", window=bouton_annule,tags="bouton_annule")

        bouton_enregs = tk.Button(self.canvas, text="Enregistrer",height=1,bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON,font=(POLICE, 11,"bold"), command=lambda: self.enregistrer())
        self.canvas.create_window(590, 863, anchor="n", window=bouton_enregs,tags="bouton_enregs")
 



    def cree_devis(self):
        if self.encien_devis is None:
            # NOUVELLE devis
            self.nouvel_devis()

        else:
            self.modifier_devis()
        
        self.canv_devis.update_idletasks()  
        self.canv_devis.config(scrollregion=self.canv_devis.bbox("all"))

    def nouvel_devis(self):
        self.info_devis()
        self.info_entrprise = InfosEntreprise(self.canv_devis,self.BDD, self.id_utilisateur)
        self.info_client = InfosClient(self.canv_devis)
        self.infos_articles = TableArticleDevis(self.canv_devis,425)
        self.infos_supplem(400)

    def modifier_devis(self):
        num_encien_devis = [self.encien_devis[0], self.encien_devis[1], self.encien_devis[6] ] # on donne la liste de [num , date , ref_client]
        self.info_devis(num_encien_devis)
        self.info_entrprise = InfosEntreprise(self.canv_devis,self.BDD, self.id_utilisateur)

        #on cherche des inofs de cleint apartir de son ref, defini dans encien devis
        requet_cl = f"SELECT * FROM client WHERE num = '{self.encien_devis[6]}' AND id_utilisateur = '{self.id_utilisateur}';"
        requet_cl = self.BDD.execute_requete(requet_cl)[0]
        self.info_client = InfosClient(self.canv_devis, requet_cl)

        table = json.loads(self.encien_devis[2])
        self.infos_articles = TableArticleDevis(self.canv_devis,425, table)

        
        position_remarque = (400 + (len(table[0]) -1 ) * 100 )
        self.infos_supplem(position_remarque, self.encien_devis[4])

        

    def info_devis(self, infos_devis=None): # infos_devis : une liste[num devis, date , ref client]
        devis_label = tk.Label(self.canv_devis, text="Devis",bg=COULEUR_LABEL,font=(POLICE, 20,"bold"))
        self.canv_devis.create_window(500, 40, anchor="n", window=devis_label)
        # Num devis
        self.num_devis = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM devis;")[0][0])
        num_devis_label = tk.Label(self.canv_devis, text="Numbre Devis : ",bg=COULEUR_LABEL)
        self.canv_devis.create_window(797, 70, anchor="n", window=num_devis_label)
        self.entry_num_devis = tk.Entry(self.canv_devis)
        self.canv_devis.create_window(925, 70, anchor="n", window=self.entry_num_devis)
        # Date devis
        date_devis_label = tk.Label(self.canv_devis, text="Date Devis : ",bg=COULEUR_LABEL)
        self.canv_devis.create_window(805,100, anchor="n", window=date_devis_label)
        self.entry_date_devis = tk.Entry(self.canv_devis)
        self.canv_devis.create_window(925, 100, anchor="n", window=self.entry_date_devis)
        #Ref client 
        self.num_client = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM client;")[0][0])
        ref_cleint_label = tk.Label(self.canv_devis, text="Ref Client : ",bg=COULEUR_LABEL)
        self.canv_devis.create_window(810,130, anchor="n", window=ref_cleint_label)
        self.entry_ref_cleint = tk.Entry(self.canv_devis)
        self.canv_devis.create_window(925, 130, anchor="n", window=self.entry_ref_cleint)

        if(infos_devis):
            self.entry_num_devis.insert(0, infos_devis[0])
            self.entry_date_devis.insert(0,infos_devis[1])
            self.entry_ref_cleint.insert(0,infos_devis[2])
        else:
            self.entry_num_devis.insert(0, f"DEV000{self.num_devis +1 }")
            self.entry_date_devis.insert(0,datetime.datetime.now().date()) #afficheer la date actule par defut
            self.entry_ref_cleint.insert(0,f"CL000{self.num_client + 1}") 

    def infos_supplem(self,y, remarqu=None):
        self.y = y
        lab_remarq = tk.Label(self.canv_devis, text="Remarque : ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_devis.create_window(100, (self.y +250) , anchor="n", window=lab_remarq,tags="remarq")
        self.text_remarq = tk.Text(self.canv_devis, bg="white", width=100,height=9)
        self.canv_devis.create_window(10, (self.y +280) , anchor="nw", window=self.text_remarq,tags="text_remarq")

        if(remarqu):
            self.text_remarq.insert(tk.END,remarqu)
        else:
            self.text_remarq.config(fg="gray")
            self.text_remarq.insert(tk.END,"Ajouter des remarques")
            self.text_remarq.bind("<FocusIn>", lambda event: effacer_Text_indicatif(self.text_remarq, "Ajouter des remarques" ))


        sing = tk.Label(self.canv_devis, text="Singature ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_devis.create_window(870, (self.y +270) , anchor="n", window=sing,tags="sing")
        bouton_sing = tk.Button(self.canv_devis, text="+",bg="black",fg="white", command=lambda: self.ajoute_singature())
        self.canv_devis.create_window(950, self.y + 270, anchor="n", window=bouton_sing,tags="ajoute_sing")

    def ajoute_singature(self):
        x, y = self.canv_devis.coords("sing")
        frame_sing = tk.Frame(self.canv_devis, width=250, height=130, bg=COULEUR_LABEL)
        self.canv_devis.create_window(850, y + 30, anchor="n", window=frame_sing,tags="frame_sing")
        SignatureFrame(self.canv_devis,frame_sing,self.id_utilisateur) 
        # on done l'id pour singateur car on relier chaque singeur avec l'utilsature actuel ,, 
        # il paux modifer comme il veux, par contre la fois qu'il singe pas on prend son dernier signature 

    def enregistrer(self):
        #on s'assore des format d'infos avant enregestrer
        num_devis = self.entry_num_devis.get() if (self.entry_num_devis.get()[0:6] =="DEV000") else f"DEV000{self.num_devis +1 }"
        date_devis = self.entry_date_devis.get()
        ref_client = self.entry_ref_cleint.get() if(self.entry_ref_cleint.get()[0:5] == "CL000") else f"CL000{self.num_client + 1}"

        donnees_client = self.info_client.get_info()
        donnees_entrpris = self.info_entrprise.get_info()
        
        donnees_articles = json.dumps(self.infos_articles.get_info()) #une liste qui contiens des liste ( chaque article represnter dans une liste) + total htt et total ttc
        montant = self.infos_articles.get_info()[2]

        remarque = self.text_remarq.get("1.0", "end-1c")

        #requet de checher d'abord si la client deaje dans BDD , sinon on va l'ajouter
        requet_cl = f"SELECT num FROM client WHERE num = '{ref_client}' AND id_utilisateur = '{self.id_utilisateur}';"
        requet_cl = self.BDD.execute_requete(requet_cl)
        if (len(requet_cl) == 0 ):
            #si le client n'est pas encore dans table client , on va l'ajouter
            requet_cl = "INSERT INTO client (num, nom, prenom, adresse, tel_fax, mobil, id_utilisateur) \
                    VALUES(%s, %s, %s, %s, %s, %s, %s )" 

            valeurs = (ref_client, donnees_client[0], donnees_client[1], donnees_client[2], donnees_client[3], donnees_client[4] , self.id_utilisateur )

            self.BDD.execute_requete(requet_cl,valeurs)
        else:
            pass #si deja existe 

        #on chereche si les info d'entreprise deja exite dans BDD , sinon on vas l'ajouter , et relier avec l'utilisateur 
        requet_entrprise = f"SELECT * FROM entreprise WHERE id_utilisateur = '{self.id_utilisateur}';"
        requet_entrprise = self.BDD.execute_requete(requet_entrprise)
        if (len(requet_entrprise) == 0 ):
            #on ajoute les infos en reliant avec l'tilisateu , pour que la prochin fois , pas obliger de sissir tous infos
            requet_entrprise = "INSERT INTO entreprise (nom_entreprise, adresse, mail, telephone, nb_ser, logo, id_utilisateur) \
                    VALUES(%s, %s, %s, %s, %s, %s, %s )"
            valeurs = (donnees_entrpris[0], donnees_entrpris[1], donnees_entrpris[2], donnees_entrpris[3], donnees_entrpris[4], donnees_entrpris[5], self.id_utilisateur)

            requet_entrprise = self.BDD.execute_requete(requet_entrprise, valeurs)
        else:
            pass #si deja existe

        #on cherche le devis par son num , si il existe deja ( pour juste modifier l'infos ) sinon on cree une nouvelle
        requet_devis = f"SELECT num FROM devis WHERE num = '{num_devis}' AND id_utilisateur = '{self.id_utilisateur}';"
        requet_devis = self.BDD.execute_requete(requet_devis)
        if ( len(requet_devis) == 0 ):
            # si elle n'existe pas ou on la cree
            requet_devis = "INSERT INTO devis (num, date_devis, intervens, montant, remarque, id_utilisateur, ref_client) \
                VALUES(%s, %s, %s, %s, %s, %s,  %s)"

            valeurs = (num_devis, date_devis, donnees_articles, montant, remarque,  self.id_utilisateur, ref_client)
            resultat = self.BDD.execute_requete(requet_devis, valeurs)

        else:
            #ici au liux de parcourir chaque infos pour update , s'il y'a des modification on va supprimer l'encien facture et on ajoute la nouvelle modifiee
            encien_val = f"DELETE FROM devis  WHERE num = '{num_devis}' AND id_utilisateur = '{self.id_utilisateur}';"
            sup_encien = self.BDD.execute_requete(encien_val)

            #on ajoute la nouvelle 
            requet_devis = "INSERT INTO devis (num, date_devis, intervens, montant, remarque, id_utilisateur, ref_client) \
                VALUES(%s, %s, %s, %s, %s, %s,  %s)"

            valeurs = (num_devis, date_devis, donnees_articles, montant, remarque,  self.id_utilisateur, ref_client)
            resultat = self.BDD.execute_requete(requet_devis, valeurs)

        self.frame_devis.destroy()
        self.canv_devis.destroy()
        self.root.event_generate("<<retour_page_devis>>")
        



    def annule(self):
        self.frame_devis.destroy()
        self.canv_devis.destroy()
        self.root.event_generate("<<retour_page_devis>>")


    def on_config(self, event):
        if (self.canvas):
            # Recalculer les dimensions de la fenêtre
            x = self.root.winfo_width()
            y = self.root.winfo_height()

            self.frame_button.config(width=x, height=(y // 11.42))
            self.frame_button.place(x=0, y=0)

            self.canvas.config(width=x, height=y)
            self.canvas.place(x=0, y=(y //11.42))

            self.frame_devis.config(width=1000, height=(y//1.176))
            self.frame_devis.place(x=(x-1000)//2, y=10)
            self.canv_devis.config(width=1000,height=(y//1.176))
