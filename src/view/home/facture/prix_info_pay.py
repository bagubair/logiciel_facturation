import tkinter as tk
import datetime


from const import *
from tools.event_entry import effacer_indicatif


class InfosPaiment():
    def __init__(self, canvas, pos_vertical,total_ht):
        self.canv_fact = canvas
        self.y = pos_vertical
        self.total_ht = total_ht

        self.info_paiment()


    
    def info_paiment(self):
        
        # Total HT, TVA, Total TTC, etc.
        total_ht_label = tk.Label(self.canv_fact, text=f"   Total HT :   {self.total_ht } € ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +70) , anchor="n", window=total_ht_label,tags="Total_HT")

        tva_label = tk.Label(self.canv_fact, text=f"      TVA :   {(self.total_ht * 0.2) } € ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +95) , anchor="n", window=tva_label,tags="TVA")

        total_ttc_label = tk.Label(self.canv_fact, text=f"   Total TTC :  {(self.total_ht * 0.2) + self.total_ht } €",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +120) , anchor="n", window=total_ttc_label,tags="Total_TTC")

        net_a_payer_label = tk.Label(self.canv_fact, text=f"  Net à payer : {(self.total_ht * 0.2) + self.total_ht } €",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +145) , anchor="n", window=net_a_payer_label,tags="Net")

        etat_fact = tk.Label(self.canv_fact, text="Facture payée : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +170) , anchor="n", window=etat_fact,tags="etat_fact")
        self.checketat_var = tk.IntVar()
        check_etat = tk.Checkbutton(self.canv_fact, variable=self.checketat_var)
        self.canv_fact.create_window(860, (self.y +170) , anchor="n", window=check_etat,tags="box_check")

        mode_paiement_label = tk.Label(self.canv_fact, text="Mode de paiement : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(840, (self.y +195) , anchor="n", window=mode_paiement_label,tags="Mode")

        self.mode_paiement = tk.StringVar()

        # Créer les boutons de contrôle pour chaque option de mode de paiement
        carte_button = tk.Checkbutton(self.canv_fact, text="Carte", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Carte", offvalue="")
        self.canv_fact.create_window(770, (self.y +213) , anchor="n", window=carte_button,tags="carte")

        cheque_button = tk.Checkbutton(self.canv_fact, text="Chèque", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Chèque", offvalue="")
        self.canv_fact.create_window(840, (self.y +213) , anchor="n", window=cheque_button,tags="cheque")

        espece_button = tk.Checkbutton(self.canv_fact, text="Espèces", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Espèces", offvalue="")
        self.canv_fact.create_window(910, (self.y +213) , anchor="n", window=espece_button,tags="espece")


        date_echange_label = tk.Label(self.canv_fact, text="Date d'échange :",bg=COULEUR_LABEL)
        self.canv_fact.create_window(780, (self.y +240) , anchor="n", window=date_echange_label,tags="date")
        self.ent_date_ech = tk.Entry(self.canv_fact,width=15)
        self.ent_date_ech.insert(0,datetime.datetime.now().date())
        self.canv_fact.create_window(900, (self.y +240) , anchor="n", window=self.ent_date_ech,tags="ent_date")



        info_banc = tk.Label(self.canv_fact, text="Informations Bancaires ",bg=COULEUR_LABEL,font=(POLICE, 15,"bold"))
        self.canv_fact.create_window(200, (self.y +70) , anchor="n", window=info_banc,tags="infos")

        banque = tk.Label(self.canv_fact, text="Banque : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(100, (self.y +95) , anchor="n", window=banque,tags="banque")
        self.ent_banque = tk.Entry(self.canv_fact,width=30)
        self.canv_fact.create_window(230, (self.y +95) , anchor="n", window=self.ent_banque,tags="ent_banque")
        
   
        rib = tk.Label(self.canv_fact, text="RIB : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(100, (self.y +120) , anchor="n", window=rib,tags="rib")
        self.ent_rib = tk.Entry(self.canv_fact,width=30)
        self.canv_fact.create_window(230, (self.y +120) , anchor="n", window=self.ent_rib,tags="ent_rib")

        iban = tk.Label(self.canv_fact, text="IBAN : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(100, (self.y +145) , anchor="n", window=iban,tags="iban")
        self.ent_iban = tk.Entry(self.canv_fact,width=30)
        self.canv_fact.create_window(230, (self.y +145) , anchor="n", window=self.ent_iban,tags="ent_iban")

        bic = tk.Label(self.canv_fact, text="BIC : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(100, (self.y +170) , anchor="n", window=bic,tags="bic")
        self.ent_bic = tk.Entry(self.canv_fact,width=30)
        self.canv_fact.create_window(230, (self.y +170) , anchor="n", window=self.ent_bic,tags="ent_bic")
   
        self.canv_fact.update_idletasks()  
        self.canv_fact.configure(scrollregion=self.canv_fact.bbox("all"))


    def get_info_pay(self):
        net = (self.total_ht * 0.2) + self.total_ht
        etat = self.checketat_var.get()  #renvoi 1 si c'est payee et 0 sinon
        mode = self.mode_paiement.get()
        date_echan = self.ent_date_ech.get()

        return [net, etat, mode, date_echan]

    def get_info_banqu(self):
        banq = self.ent_banque.get()
        rib = self.ent_rib.get()
        iban = self.ent_iban.get()
        bic = self.ent_bic.get()

        return [banq, rib, iban, bic]

