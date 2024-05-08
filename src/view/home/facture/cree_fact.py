import tkinter as tk
import json

from PIL import Image,ImageTk, ImageDraw
from tkinter import filedialog
import datetime


from const import *
from tools.event_entry import effacer_indicatif

from view.home.facture.infos_client import InfosClient
from view.home.facture.infos_entrprise import InfosEntreprise
from view.home.facture.table_article import TableArticle
from view.home.facture.prix_info_pay import InfosPaiment
from view.home.facture.singature import SignatureFrame


class Facture:
    def __init__(self, root,frame_button,BDD, id_utilisateur):
        self.root = root
        self.frame_button = frame_button
        self.BDD = BDD
        self.id_utilisateur = id_utilisateur
        
        self.root.after(10, self.initialisation)
        self.root.bind("<Configure>", self.on_configure)
        
        

        
    def initialisation(self):

        self.x = self.root.winfo_width()
        self.y = self.root.winfo_height()

        self.canvas = tk.Canvas(self.root, width=self.x, height=self.y,bg=COULEUR_PRINCIPALE)
        self.canvas.place(x=0, y=(self.y //11.42))

        self.frame_fact = tk.Frame(self.canvas, width=(self.x//1.2), height=(self.y//1.151), bg=COULEUR_LABEL)
        self.frame_fact.grid_propagate(False)  # Empêcher le frame de redimensionner ses cellules
        self.frame_fact.place(x=100, y=0)

        # Création du canevas avec la barre de défilement
        self.canv_fact = tk.Canvas(self.frame_fact,width=(self.x//1.2), height=(self.y//1.151), yscrollincrement=8, bg=COULEUR_LABEL)
        self.canv_fact.grid_propagate(False)
        self.scrol_fact = tk.Scrollbar(self.frame_fact, command=self.canv_fact.yview, orient="vertical", bg=COULEUR_PRINCIPALE)
        self.scrol_fact.pack(side="right", fill="y")
        self.canv_fact.configure(yscrollcommand=self.scrol_fact.set)
        self.canv_fact.pack(side=tk.TOP, expand=True, fill=tk.BOTH)  # Remplir le canevas avec tout l'espace disponible
       

        self.cree_facture()
        self.event_entry_case()
        




    def on_configure(self, event):
        if (self.canvas):
            # Recalculer les dimensions de la fenêtre
            x = self.root.winfo_width()
            y = self.root.winfo_height()

            self.frame_button.config(width=x, height=(y // 11.42))
            self.frame_button.place(x=0, y=0)

            self.canvas.config(width=x, height=y)
            self.canvas.place(x=0, y=(y //11.42))

            self.frame_fact.config(width=1000, height=(y-80))
            self.frame_fact.place(x=(x-1000)//2, y=10)
            self.canv_fact.config(width=1000,height=(y-80))

            

    
    def cree_facture(self):
        # FACTURE
        self.info_facture()

        self.info_entrprise = InfosEntreprise(self.canv_fact)
        self.info_client = InfosClient(self.canv_fact)
        self.info_table_articles = TableArticle(self.canv_fact,425)

        total_ht = self.info_table_articles.get_info()[1]
        self.info_paiment = InfosPaiment(self.canv_fact,540, total_ht )

        self.infos_supplem()

        self.canv_fact.update_idletasks()  
        self.canv_fact.configure(scrollregion=self.canv_fact.bbox("all"))


    def info_facture(self):
        facture_label = tk.Label(self.canv_fact, text="FACTURE",bg=COULEUR_LABEL,font=(POLICE, 20,"bold"))
        self.canv_fact.create_window(500, 40, anchor="n", window=facture_label)
        
        # Num facture
        num_fact = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM facture;")[0][0])
        num_facture_label = tk.Label(self.canv_fact, text="Numbre facture : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(797, 70, anchor="n", window=num_facture_label)
        self.entry_num_fact = tk.Entry(self.canv_fact,fg="gray")
        self.canv_fact.create_window(925, 70, anchor="n", window=self.entry_num_fact)
        self.entry_num_fact.insert(0, f"FAC000{num_fact +1 }")
        
        # Date facture
        date_facture_label = tk.Label(self.canv_fact, text="Date facture : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(805,100, anchor="n", window=date_facture_label)
        self.entry_date_fact = tk.Entry(self.canv_fact)
        self.entry_date_fact.insert(0,datetime.datetime.now().date()) #afficheer la date actule par defut
        self.canv_fact.create_window(925, 100, anchor="n", window=self.entry_date_fact)

        #Ref client 
        num_client = int(self.BDD.execute_requete(f"SELECT COUNT(*) AS nombre_de_lignes FROM client;")[0][0])
        ref_cleint_label = tk.Label(self.canv_fact, text="Ref Client : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(810,130, anchor="n", window=ref_cleint_label)
        self.entry_ref_cleint = tk.Entry(self.canv_fact)
        self.entry_ref_cleint.insert(0,f"CL000{num_client + 1}") 
        self.canv_fact.create_window(925, 130, anchor="n", window=self.entry_ref_cleint)
        
    
    

    
    def infos_supplem(self):
        self.y = 540
        remarq = tk.Label(self.canv_fact, text="Remarque : ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_fact.create_window(100, (self.y +250) , anchor="n", window=remarq,tags="remarq")
        self.text_remarq = tk.Text(self.canv_fact, bg="white", width=120,height=4,fg="gray")
        self.canv_fact.create_window(10, (self.y +280) , anchor="nw", window=self.text_remarq,tags="text_remarq")

        sing = tk.Label(self.canv_fact, text="Singature ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_fact.create_window(870, (self.y +380) , anchor="n", window=sing,tags="sing")
        bouton_sing = tk.Button(self.canv_fact, text="+",bg="black",fg="white", command=lambda: self.ajoute_singature())
        self.canv_fact.create_window(950, self.y + 380, anchor="n", window=bouton_sing,tags="ajoute_sing")

        

        bouton_annule = tk.Button(self.canv_fact, text="Annuler",height=2,bg=COULEUR_CANVAS,font=(POLICE, 13,"bold"), command=lambda: self.annule())
        self.canv_fact.create_window(425, self.y + 520, anchor="n", window=bouton_annule,tags="bouton_annule")

        bouton_enregs = tk.Button(self.canv_fact, text="Enregistrer",height=2,bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON,font=(POLICE, 13,"bold"), command=lambda: self.enregistrer())
        self.canv_fact.create_window(550, self.y + 520, anchor="n", window=bouton_enregs,tags="bouton_enregs")

    def ajoute_singature(self):
        x, y = self.canv_fact.coords("sing")
        frame_sing = tk.Frame(self.canv_fact, width=250, height=130, bg=COULEUR_LABEL)
        self.canv_fact.create_window(850, y + 30, anchor="n", window=frame_sing,tags="frame_sing")
        SignatureFrame(self.canv_fact,frame_sing,self.id_utilisateur) 
        # on done l'id pour singateur car on relier chaque singeur avec l'utilsature actuel ,, 
        # il paux modifer comme il veux, par contre la fois qu'il singe pas on prend son dernier signature 


    def enregistrer(self):
        num_fact = self.entry_num_fact.get()
        date_fact = self.entry_date_fact.get()
        ref_client = self.entry_ref_cleint.get()

        donnees_client = self.info_client.get_info()
        donnees_entrpris = self.info_entrprise.get_info()
        donnees_articles = json.dumps(self.info_table_articles.get_info())
        doonees_banque = self.info_paiment.get_info_banqu()
        donnees_payee = self.info_paiment.get_info_pay()[2]

        etat_facture = self.info_paiment.get_info_pay()[1]
        net = self.info_paiment.get_info_pay()[0]

        remarque = self.text_remarq.get("1.0", "end-1c")

        if( os.path.join(DATA_DIR, f"signature_{self.id_utilisateur}.png") ):
            signature = os.path.join(DATA_DIR, f"signature_{self.id_utilisateur}.png")
        else:
            signature = None

        #requet de checher d'abord si la client deaje dans BDD , sinon on va l'ajouter
        requet_cl = f"SELECT num FROM client WHERE num = '{ref_client}';"
        requet_cl = self.BDD.execute_requete(requet_cl)
        if (len(requet_cl) == 0 ):
            #si le client n'est pas encore dans table client , on va l'ajouter
            requet_cl = f"INSERT INTO client (num, nom, prenom, adresse, tel_fax, mobil, id_utilisateur) \
                    VALUES('{ref_client}', '{donnees_client[0]}', '{donnees_client[1]}', '{donnees_client[2]}', '{donnees_client[3]}', '{donnees_client[4]}' , '{self.id_utilisateur}' )"
            self.BDD.execute_requete(requet_cl)
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

        #on cherche la facture par son num , si il existe deja ( pour juste modifier l'infos ) sinon on cree une nouvelle
        requet_fact = f"SELECT num FROM facture WHERE num = '{num_fact}';"
        requet_fact = self.BDD.execute_requete(requet_fact)
        if ( len(requet_fact) == 0 ):
            # si elle n'existe pas ou on la cree
            requet_fact = "INSERT INTO facture (num, date_fac, intervens, remarque, etat_fac, net_pay,info_pay, infos_banque, sign, id_utilisateur, ref_client) \
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            valeurs = (num_fact, date_fact, donnees_articles, remarque, etat_facture, net, donnees_payee, doonees_banque, signature, self.id_utilisateur, ref_client)
            resultat = self.BDD.execute_requete(requet_fact, valeurs)

        else:
            encien_val = f"DELETE FROM facture WHERE num = '{num_fact}'';"
            sup_encien = self.BDD.execute_requete(encien_val)

            #on ajoute la nouvelle 
            requet_fact = "INSERT INTO facture (num, date_fac, intervens, remarque, etat_fac, net_pay,info_pay, infos_banque, sign, id_utilisateur, ref_client) \
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            valeurs = (num_fact, date_fact, donnees_articles, remarque, etat_facture, net, donnees_payee, doonees_banque, signature, self.id_utilisateur, ref_client)
            resultat = self.BDD.execute_requete(requet_fact, valeurs)
        self.frame_fact.destroy()
        self.canv_fact.destroy()
        self.root.event_generate("<<retour_history_fact>>")


    def annule(self):
        self.frame_fact.destroy()
        self.canv_fact.destroy()
        self.root.event_generate("<<retour_history_fact>>")




    def event_entry_case(self):
        """on active l'event pour case enrty pour quand l'utilisateur tape le case , l'example existe va supprimer 
            par la fonction importée (effacer_indicatif) qui prend le variable Entry et son text indicatif
        """

        self.entry_num_fact.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_num_fact,"FAC0001"))
        
        
        #self.entry_coment_client.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_coment_client, "Commentaire libre"))
        

    