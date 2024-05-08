import tkinter as tk
import datetime


from const import *
from tools.event_entry import effacer_indicatif


class InfosClient():
    def __init__(self, canvas):

        self.canv_fact = canvas
        self.info_client()
        self.event_entry_case()



    def info_client(self):
        client = tk.Label(self.canv_fact, text="Adresse De Facturation : ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_fact.create_window(760, 185, anchor="n", window=client)
        # Adresse client
        nom_client_label = tk.Label(self.canv_fact, text="Nom : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(710, 215, anchor="n", window=nom_client_label)
        self.entry_nom_client = tk.Entry(self.canv_fact,width=35,fg="gray")
        self.entry_nom_client.insert(0, "Nom Client ")
        self.canv_fact.create_window(870, 215, anchor="n", window=self.entry_nom_client)

        pren_client_label = tk.Label(self.canv_fact, text="Prénom : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(710, 240, anchor="n", window=pren_client_label)
        self.entry_pren_client = tk.Entry(self.canv_fact,width=35,fg="gray")
        self.entry_pren_client.insert(0, "Prénom Client ")
        self.canv_fact.create_window(870, 240, anchor="n", window=self.entry_pren_client)
        
        adresse_client_label = tk.Label(self.canv_fact, text="Adresse : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(710, 265, anchor="n", window=adresse_client_label)
        self.entry_adrs_client = tk.Entry(self.canv_fact,width=35,fg="gray")
        self.entry_adrs_client.insert(0, "Rue ....")
        self.canv_fact.create_window(870, 265, anchor="n", window=self.entry_adrs_client)

        telphon_client_label = tk.Label(self.canv_fact, text="Tél.fixe : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(710, 290, anchor="n", window=telphon_client_label)
        self.entry_tel_client = tk.Entry(self.canv_fact,width=35,fg="gray")
        self.entry_tel_client.insert(0, "(123) 456 789")
        self.canv_fact.create_window(870, 290, anchor="n", window=self.entry_tel_client)

        mobil_client_label = tk.Label(self.canv_fact, text="Tél Mobile : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(710, 315, anchor="n", window=mobil_client_label)
        self.entry_mobil_client = tk.Entry(self.canv_fact, width=35, fg="gray")
        self.entry_mobil_client.insert(0, "(123) 456 789")
        self.canv_fact.create_window(870, 315, anchor="n", window=self.entry_mobil_client)


    def event_entry_case(self):
        """on active l'event pour case enrty pour quand l'utilisateur tape le case , l'example existe va supprimer 
            par la fonction importée (effacer_indicatif) qui prend le variable Entry et son text indicatif
        """
        self.entry_nom_client.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_nom_client, "Nom Client " ))
        self.entry_pren_client.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_pren_client, "Prénom Client "))
        self.entry_adrs_client.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_adrs_client, "Rue ...."))
        self.entry_tel_client.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_tel_client, "(123) 456 789"))


    def get_info(self):
        nom = self.entry_nom_client.get()
        prenom = self.entry_pren_client.get()
        adr = self.entry_adrs_client.get()
        tel = self.entry_tel_client.get()
        mobil = self.entry_mobil_client.get()

        return [nom,prenom,adr,tel,mobil]



