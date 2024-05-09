import tkinter as tk

from const import *

from view.home.facture.cree_fact import Facture
from view.home.facture.touts_facture import ToutesFacture

class HistoryFacture:
    def __init__(self, root,frame_button,BDD, id_utilisateur):
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
        self.canvas.place(x=0, y=(y//11.42))

        self.lis_button_fact = [] # on mettre les button dans une liste pour appliquer le chnagement de couleur de phase active.
        self.button_active = 0

        self.tout_fact = tk.Button(self.canvas, width=20, height=3,text="Toutes les factures", command=lambda:self.touts_facture() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 10,"bold"))
        self.tout_fact.place(x=(x//30), y=(y//32))
        self.lis_button_fact.append(self.tout_fact)

        self.fact_payee = tk.Button(self.canvas, width=20, height=3,text="Factures payées", command=lambda:self.facture_payee() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 10,"bold"))
        self.fact_payee.place(x=(x//5.33), y=(y//32))
        self.lis_button_fact.append(self.fact_payee)

        self.fact_non_payee = tk.Button(self.canvas, width=20, height=3,text="Factures non payées", command=lambda:self.facture_non_payee() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 10,"bold"))
        self.fact_non_payee.place(x=(x//3), y=(y//32))
        self.lis_button_fact.append(self.fact_non_payee)


        self.nouvel_fact = tk.Button(self.canvas, width=20, height=2,text="Nouvelle facture", command=lambda:self.nouvelle_facture() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 9,"bold"))
        self.canvas.create_window((x//1.0169), (y//22.85) , anchor="ne", window=self.nouvel_fact,tags="nouvl_fact")

        self.recherhe_fact = tk.Entry(self.canvas,width=22,fg="gray")
        self.canvas.create_window((x//1.2), (y//14.54) , anchor="ne", window=self.recherhe_fact,tags="rech_fact")
        self.recherhe_fact.insert(0, "Recherche")
        

        fact = tk.Label(self.canvas, text="Facture",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(140, 160 , anchor="n", window=fact,tags="fact")
        client = tk.Label(self.canvas, text="Client",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(380, 160 , anchor="n", window=client,tags="client")
        date = tk.Label(self.canvas, text="Date",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(600, 160 , anchor="n", window=date,tags="date")
        solde = tk.Label(self.canvas, text="Solde Dû ",bg=COULEUR_PRINCIPALE, font=(POLICE,12,"bold"))
        self.canvas.create_window(850,160 , anchor="n", window=solde,tags="solde")
        

        # Création de la listebox
        self.listbox = tk.Listbox(self.canvas, selectmode=tk.SINGLE,  width=650, height=400,font=(POLICE,10))
        self.canvas.create_window(500, 200, width=950, height=400, anchor="n", window=self.listbox, tags="listbox")

        self.lire = tk.Button(self.canvas, width=10, height=2,text="Lire", command=lambda:self.lire_fact() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(390,610 , anchor="n", window=self.lire,tags="lire")
        
        self.modf = tk.Button(self.canvas, width=10, height=2,text="Modifier", command=lambda:self.modf_fact() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(510,610 , anchor="n", window=self.modf,tags="lire")
        
        self.supprim = tk.Button(self.canvas, width=10, height=2,text="Supprimer", command=lambda:self.supprim_fact() ,bg=COULEUR_PRINCIPALE,font=(POLICE, 11,"bold"))
        self.canvas.create_window(630,610 , anchor="n", window=self.supprim,tags="lire")
        


        self.requet_tous_fact = f"SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay FROM client, facture WHERE client.num = facture.ref_client AND facture.id_utilisateur = {self.id_utilisateur}"
        self.requet_tous_fact = self.BDD.execute_requete(self.requet_tous_fact)

        self.requt_fact_non_pay = f"SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay FROM client, facture WHERE client.num = facture.ref_client AND facture.id_utilisateur = {self.id_utilisateur} AND facture.etat_fac = 0"
        self.requt_fact_non_pay = self.BDD.execute_requete(self.requt_fact_non_pay)

        self.requt_fact_pay = f"SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay FROM client, facture WHERE client.num = facture.ref_client AND facture.id_utilisateur = {self.id_utilisateur} AND facture.etat_fac = 1"
        self.requt_fact_pay = self.BDD.execute_requete(self.requt_fact_pay)

        self.touts_facture() #on ititialse le page pour tous facture


        self.recherhe_fact.bind("<Return>",lambda event: self.cherche_facture())
        



    def touts_facture(self):
        self.lis_button_fact[self.button_active].config(bg=COULEUR_PRINCIPALE)
        self.lis_button_fact[0].config(bg=COULEUR_CANVAS)
        self.button_active = 0

    

        self.listbox.delete(0, tk.END)
        for fact in self.requet_tous_fact:
            nom_client = f"{fact[1]} {fact[2]}"

            format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
            self.listbox.insert(tk.END, format_info)

        
    def facture_payee(self):
        self.lis_button_fact[self.button_active].config(bg=COULEUR_PRINCIPALE)
        self.lis_button_fact[1].config(bg=COULEUR_CANVAS)
        self.button_active = 1
        
        self.listbox.delete(0, tk.END)
        for fact in self.requt_fact_pay:
            nom_client = f"{fact[1]} {fact[2]}"

            format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
            self.listbox.insert(tk.END, format_info)

    def facture_non_payee(self):
        self.lis_button_fact[self.button_active].config(bg=COULEUR_PRINCIPALE)
        self.lis_button_fact[2].config(bg=COULEUR_CANVAS)
        self.button_active = 2
        
        self.listbox.delete(0, tk.END)
        for fact in self.requt_fact_non_pay:
            nom_client = f"{fact[1]} {fact[2]}"

            format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
            self.listbox.insert(tk.END, format_info)

    def nouvelle_facture(self):
        self.canvas.destroy()
        Facture(self.root,self.frame_button,self.BDD, self.id_utilisateur) #defini dans  (cree_fact.py)


    def cherche_facture(self, event=None):

        if ( self.button_active ==0 ):

            requete_cherche = f"""
                        SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay
                        FROM client
                        INNER JOIN facture ON client.num = facture.ref_client
                        WHERE 
                        facture.id_utilisateur = '{self.id_utilisateur}' AND (
                        facture.num = '{self.recherhe_fact.get()}' OR
                        client.nom = '{self.recherhe_fact.get()}' OR
                        client.prenom = '{self.recherhe_fact.get()}' OR
                        facture.date_fac = '{self.recherhe_fact.get()}'
                    )
                    """
            resultat_recherche = self.BDD.execute_requete(requete_cherche)

            self.listbox.delete(0, tk.END)
            for fact in resultat_recherche:
                nom_client = f"{fact[1]} {fact[2]}"

                format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
                self.listbox.insert(tk.END, format_info)

        elif( self.button_active == 1):
            requete_cherche = f"""
                        SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay
                        FROM client
                        INNER JOIN facture ON client.num = facture.ref_client
                        WHERE facture.etat_fac = 1 
                        AND facture.id_utilisateur = '{self.id_utilisateur}' AND (
                        facture.num = '{self.recherhe_fact.get()}' OR
                        client.nom = '{self.recherhe_fact.get()}' OR
                        client.prenom = '{self.recherhe_fact.get()}' OR
                        facture.date_fac = '{self.recherhe_fact.get()}'
                    )
                    """
            resultat_recherche = self.BDD.execute_requete(requete_cherche)

            self.listbox.delete(0, tk.END)
            for fact in resultat_recherche:
                nom_client = f"{fact[1]} {fact[2]}"

                format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
                self.listbox.insert(tk.END, format_info)

        else:
            requete_cherche = f"""
                        SELECT facture.num, client.nom, client.prenom, facture.date_fac, facture.net_pay
                        FROM client
                        INNER JOIN facture ON client.num = facture.ref_client
                        WHERE facture.etat_fac = 0 
                        AND facture.id_utilisateur = '{self.id_utilisateur}' AND (
                        facture.num = '{self.recherhe_fact.get()}' OR
                        client.nom = '{self.recherhe_fact.get()}' OR
                        client.prenom = '{self.recherhe_fact.get()}' OR
                        facture.date_fac = '{self.recherhe_fact.get()}'
                    )
                    """
            resultat_recherche = self.BDD.execute_requete(requete_cherche)

            self.listbox.delete(0, tk.END)
            for fact in resultat_recherche:
                nom_client = f"{fact[1]} {fact[2]}"

                format_info = f"{'':<27}{fact[0]:<60}{nom_client:<53}{fact[3]:<60}{fact[4]:>20}"
                self.listbox.insert(tk.END, format_info)


    def lire_fact(self):
        pass

    def modf_fact(self):
        pass

    def supprim_fact(self):
        pass

    
    
    def on_configure(self, event):
        if (self.canvas):
            # Recalculer les dimensions de la fenêtre
            long = self.root.winfo_width()
            haut = self.root.winfo_height()
            self.frame_button.config(width=long, height=(haut // 11.42))
            self.frame_button.place(x=0, y=0)

            self.canvas.config(width=long, height=haut)
            self.canvas.place(x=0, y=(haut // 11.42))

            self.canvas.coords("nouvl_fact",(long//1.0169), (haut//22.85))
            self.canvas.coords("rech_fact",(long//1.2), (haut//14.54))
            
