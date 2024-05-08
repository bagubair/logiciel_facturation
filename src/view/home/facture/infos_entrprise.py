import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk, ImageDraw
import datetime


from const import *
from tools.event_entry import effacer_indicatif
from tools.image_size import size_photo



class InfosEntreprise():
    def __init__(self,canvas):
        self.canv_fact = canvas

        self.image_logo = None #ici pour faire referance de l'image pour son affichage 
        self.chemin_logo = None
        self.info_entrprise()
        self.event_entry_case()

        self.canv_fact.tag_bind(self.logo, "<Button-1>", self.choisir_photo)


    def info_entrprise(self):
        # Logo entreprise
        self.logo = self.canv_fact.create_rectangle(15, 20, 270, 170, fill=COULEUR_PRINCIPALE,tags="logo")
        # Ajout d'un label sur le rectangle
        self.label_logo = self.canv_fact.create_text(140, 95, text="Ajoute Logo", font=("Arial", 10),tags="click")
        
        
        
        expredature = tk.Label(self.canv_fact, text="De : ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_fact.create_window(50, 185, anchor="n", window=expredature)
        
        # Nom entreprise
        nom_entreprise_label = tk.Label(self.canv_fact, text="Nom : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(60, 215, anchor="n", window=nom_entreprise_label)
        self.entry_nom = tk.Entry(self.canv_fact,width=30,fg="gray")
        self.entry_nom.insert(0, "Nom Entreprise")
        self.canv_fact.create_window(195, 215, anchor="n", window=self.entry_nom)
        
        # Adresse entreprise
        adresse_entreprise_label = tk.Label(self.canv_fact, text="Adresse:",bg=COULEUR_LABEL)
        self.canv_fact.create_window(60, 240, anchor="n", window=adresse_entreprise_label)
        self.entry_adrs_entr = tk.Entry(self.canv_fact,width=30,fg="gray")
        self.entry_adrs_entr.insert(0, "Rue ....")
        self.canv_fact.create_window(195, 240, anchor="n", window=self.entry_adrs_entr)
        mail_entreprise_label = tk.Label(self.canv_fact, text="Mail : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(60, 265, anchor="n", window=mail_entreprise_label)
        self.entry_mail_entr = tk.Entry(self.canv_fact,width=30,fg="gray")
        self.entry_mail_entr.insert(0, "contacte@nom.fr")
        self.canv_fact.create_window(195, 265, anchor="n", window=self.entry_mail_entr)
        telphon_entreprise_label = tk.Label(self.canv_fact, text="Tél.fixe:",bg=COULEUR_LABEL)
        self.canv_fact.create_window(60, 290, anchor="n", window=telphon_entreprise_label)
        self.entry_tel_entr =tk.Entry(self.canv_fact,width=30,fg="gray")
        self.entry_tel_entr.insert(0, "(123) 456 789")
        self.canv_fact.create_window(195, 290, anchor="n", window=self.entry_tel_entr)

        N_siren_label = tk.Label(self.canv_fact, text="N° SIREN/SIRET",bg=COULEUR_LABEL)
        self.canv_fact.create_window(60, 315, anchor="n", window=N_siren_label)
        self.entry_siren_entr = tk.Entry(self.canv_fact,width=28,fg="gray")
        self.entry_siren_entr.insert(0, "Gt; 123-45-6789")
        self.canv_fact.create_window(205, 315, anchor="n", window=self.entry_siren_entr)

        

    def event_entry_case(self):
        """on active l'event pour case enrty pour quand l'utilisateur tape le case , l'example existe va supprimer 
            par la fonction importée (effacer_indicatif) qui prend le variable Entry et son text indicatif
        """
        self.entry_nom.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_nom,"Nom Entreprise"))
        self.entry_adrs_entr.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_adrs_entr,"Rue ...."))
        self.entry_mail_entr.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_mail_entr,  "contacte@nom.fr"))
        self.entry_tel_entr.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_tel_entr, "(123) 456 789"))
        self.entry_siren_entr.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_siren_entr, "Gt; 123-45-6789"))

    def get_info(self):
        nom = self.entry_nom.get()
        adr = self.entry_adrs_entr.get()
        mail = self.entry_mail_entr.get()
        tel = self.entry_tel_entr.get()
        nb_ser = self.entry_siren_entr.get()

        logo = self.chemin_logo

        return [nom, adr, mail, tel, nb_ser, logo]

    def choisir_photo(self, event=None):
        #self.canv_fact.delete("click")
        self.chemin_logo = filedialog.askopenfilename(
            title="Choisir une photo",
            filetypes=(("Fichiers PNG", "*.png"), ("Fichiers JPEG", "*.jpg;*.jpeg"), ("Tous les fichiers", "*.*"))
        )
        if self.chemin_logo:
            try:
                # Ouvrir l'image avec PIL
                self.image_logo = size_photo(self.chemin_logo, 220,150)
                if self.logo:
                    self.canv_fact.delete("logo")
                # Créer une nouvelle image sur le canevas
                self.logo = self.canv_fact.create_image(20, 30, anchor='nw', image=self.image_logo, tags="logo")
            
            except Exception as e:
                print("Erreur lors du chargement de l'image :", e)
