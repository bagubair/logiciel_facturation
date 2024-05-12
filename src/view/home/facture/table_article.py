import tkinter as tk
import json
import datetime

from const import *
from tools.event_entry import effacer_indicatif,effacer_Text_indicatif
from tools.est_nombre import est_nombre
from view.home.facture.article import Article



class TableArticle():
    def __init__(self,canvas,pos_vertical, encien_valeur_table=None, encien_val_pay=None):

        self.canv_fact = canvas
        self.y = pos_vertical
        self.encien_valeur_table = encien_valeur_table
        self.encien_val_pay = encien_val_pay

        self.total_ht = 0.0
        self.total_ttc = 0.0

        self.info_table_articles()
        self.inite_infos_pay()

        self.entr_remise.bind("<FocusOut>", self.modif_net_payer)
        self.entr_remise.bind("<Return>", self.modif_net_payer)


    def info_table_articles(self):
        ligne_1 = self.canv_fact.create_line(15, 380, 990, 380, fill="black")

        # Entête du tableau
        inter = tk.Label(self.canv_fact, text="Intervention",bg=COULEUR_LABEL)
        self.canv_fact.create_window(200, 385, anchor="n", window=inter)
        prix = tk.Label(self.canv_fact, text="Prix Unit HT",bg=COULEUR_LABEL)
        self.canv_fact.create_window(600, 385, anchor="n", window=prix)
        qunt = tk.Label(self.canv_fact, text="Quantité",bg=COULEUR_LABEL)
        self.canv_fact.create_window(680, 385, anchor="n", window=qunt)

        tout_ht = tk.Label(self.canv_fact, text="Total HT",bg=COULEUR_LABEL)
        self.toutht_id = self.canv_fact.create_window(760, 385, anchor="n", window=tout_ht)

        tva = tk.Label(self.canv_fact, text="TVA  %",bg=COULEUR_LABEL)
        self.canv_fact.create_window(840, 385, anchor="n", window=tva)

        total_ttc = tk.Label(self.canv_fact, text="Total TTC",bg=COULEUR_LABEL)
        self.canv_fact.create_window(920, 385, anchor="n", window=total_ttc)

        ligne_2 = self.canv_fact.create_line(15,415, 990, 415, fill="black")
        self.nb = 0 #pour conter numbre des article

        if(self.encien_valeur_table): 
            self.list_article = self.encien_valeur_table
            for encien_art in self.list_article:
                Article(self.canv_fact, self.y, self.nb,self, encien_art)
                self.y += 100
                self.nb += 1 #pour conter numbre des article

        else:
            self.list_article = []
            self.ajoute_article()

        bouton_ajout = tk.Button(self.canv_fact, text="+",bg="black",fg="white", command=lambda: self.ajoute_article())
        self.canv_fact.create_window(20, self.y, anchor="nw", window=bouton_ajout,tags="ajoute")

        ligne_3 = self.canv_fact.create_line(15,self.y +40 , 990,self.y+40,tags="linge_3", fill="black")

        
        
        
    
    def inite_infos_pay(self):
        # Total HT, TVA, Total TTC, etc.
        self.total_ht_label = tk.Label(self.canv_fact, bg=COULEUR_LABEL)
        self.canv_fact.create_window(860, (self.y +85) , anchor="n", window=self.total_ht_label,tags="Total_HT")

        self.total_ttc_label = tk.Label(self.canv_fact,bg=COULEUR_LABEL)
        self.canv_fact.create_window(860, (self.y +110) , anchor="n", window=self.total_ttc_label,tags="Total_TTC")

        remise = tk.Label(self.canv_fact, text=f"Remise :",bg=COULEUR_LABEL)
        self.canv_fact.create_window(840, (self.y +135) , anchor="n", window=remise,tags="remise")
        self.entr_remise = tk.Entry(self.canv_fact,width=7)
        self.canv_fact.create_window(900, (self.y +135) , anchor="n", window=self.entr_remise,tags="entr_remise")

        

        mont_remise = (self.entr_remise.get()) if (est_nombre(self.entr_remise.get()) ) else "0"
        self.net_a_payer_label = tk.Label(self.canv_fact, text=f"  Net à payer  :  {self.total_ttc - float(mont_remise) } €",bg=COULEUR_LABEL)
        self.canv_fact.create_window(860, (self.y +160) , anchor="n", window=self.net_a_payer_label,tags="Net")


        etat_fact = tk.Label(self.canv_fact, text="Facture payée : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(850, (self.y +185) , anchor="n", window=etat_fact,tags="etat_fact")
        self.checketat_var = tk.IntVar()
        check_etat = tk.Checkbutton(self.canv_fact, variable=self.checketat_var)
        self.canv_fact.create_window(900, (self.y +185) , anchor="n", window=check_etat,tags="box_check")

        mode_paiement_label = tk.Label(self.canv_fact, text="Mode de paiement : ",bg=COULEUR_LABEL)
        self.canv_fact.create_window(865, (self.y +210) , anchor="n", window=mode_paiement_label,tags="Mode")

        self.mode_paiement = tk.StringVar()

        # Créer les boutons de contrôle pour chaque option de mode de paiement
        carte_button = tk.Checkbutton(self.canv_fact, text="Carte", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Carte", offvalue="")
        self.canv_fact.create_window(780, (self.y +230) , anchor="n", window=carte_button,tags="carte")

        cheque_button = tk.Checkbutton(self.canv_fact, text="Chèque", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Chèque", offvalue="")
        self.canv_fact.create_window(850, (self.y +230) , anchor="n", window=cheque_button,tags="cheque")

        espece_button = tk.Checkbutton(self.canv_fact, text="Espèces", bg=COULEUR_LABEL, variable=self.mode_paiement, onvalue="Espèces", offvalue="")
        self.canv_fact.create_window(920, (self.y +230) , anchor="n", window=espece_button,tags="espece")


        date_echange_label = tk.Label(self.canv_fact, text="Date d'échange :",bg=COULEUR_LABEL)
        self.canv_fact.create_window(800, (self.y +255) , anchor="n", window=date_echange_label,tags="date")
        self.ent_date_ech = tk.Entry(self.canv_fact,width=15)
        self.ent_date_ech.insert(0,datetime.datetime.now().date())
        self.canv_fact.create_window(920, (self.y +255) , anchor="n", window=self.ent_date_ech,tags="ent_date")

        if (self.encien_val_pay):
            self.total_ht_label.config(text=f"   Total HT :   {self.encien_val_pay[0] } € ")
            self.total_ttc_label.config(text=f"   Total TTC :  {self.encien_val_pay[1] } €")
            self.entr_remise.insert(0,self.encien_val_pay[2])
            self.net_a_payer_label.config(text=f"  Net à payer  :  { self.encien_val_pay[1] - self.encien_val_pay[2]} €")


        else:
            self.total_ht_label.config(text=f"   Total HT :   {self.total_ht } € ")
            self.total_ttc_label.config(text=f"   Total TTC :  {self.total_ttc } €")

            self.entr_remise.config(fg="gray")
            self.entr_remise.insert(0, "0")
            self.entr_remise.bind("<FocusIn>", lambda event: effacer_indicatif(self.entr_remise, "0" ))


    def ajoute_article(self):
        new_article = Article(self.canv_devis, self.y, self.nb, self)
        self.list_article.append(new_article)
        self.nb += 1

        """ on mise a jour la postion de button ajoute ,, et tous les position suivant a lui """
        self.y += 100
        #Nouvelles coordonnées pour le bouton
        self.canv_fact.coords("ajoute", 20, self.y)
        self.canv_fact.coords("linge_3",15,self.y +40 , 990,self.y+40)
        self.update_places(self.y)

        self.canv_fact.update_idletasks()  
        self.canv_fact.configure(scrollregion=self.canv_fact.bbox("all"))


    def supprime_article(self, indx):
        #print("indx",indx)
        new_y = self.list_article[indx].supprime(indx)
        if indx != (len(self.list_article)-1):
            for i in range(indx+1 , len(self.list_article)):
                #print("i :", i)
                self.list_article[i].mise_jour(i, new_y)
                self.list_article[i].modif_tags(i, i-1)

        self.list_article.pop(indx)
        self.nb -= 1

        self.canv_fact.coords("ajoute", 20, new_y)
        self.canv_fact.coords("linge_3",15,new_y +40 , 990,new_y+40)
        self.update_places(new_y)

        self.canv_fact.update_idletasks()  
        self.canv_fact.configure(scrollregion=self.canv_fact.bbox("all"))


        #article_sup = self.canv_fact.find_withtag(f"article_{indx}")
        #self.canv_fact.delete(article_sup)
        #self.y -= 110


    def get_info(self):
        articles = []
        total_ht = 0
        total_ttc = 0
        if(self.encien_valeur_table):
            articles.append(self.encien_valeur_table)
            self.total_ht += self.encien_val_pay[0]
            self.total_ttc += self.encien_val_pay[1]
            #pour nouvelle class ajoute , on appel comme une class ,;;; on parcourir dans notre liste par indice, aprtier de premier nouvelle article
            for idx_new_article in range(len(self.encien_valeur_table) , len(self.list_article)):
                articles.append(self.list_article[idx_new_article].get_info())
                self.total_ht += self.list_article[idx_new_article].get_info()[4]
                self.total_ttc += self.list_article[idx_new_article].get_info()[5]
            
        else:
            for atricle in self.list_article:
                articles.append(atricle.get_info())
                total_ht += atricle.get_info()[4]
                total_ttc += atricle.get_info()[5]

        remis =float( self.entr_remise.get()) if (est_nombre(self.entr_remise.get()) ) else "0"
        net = total_ttc - remis 
        etat = self.checketat_var.get()  #renvoi 1 si c'est payee et 0 sinon
        mode = self.mode_paiement.get()
        date_echan = self.ent_date_ech.get()

        return [articles, total_ht, total_ttc,remis,net, etat, mode, date_echan]

    def calcule_total(self):
        self.total_ht = 0
        self.total_ttc = 0
        if(self.encien_valeur_table):
            self.total_ht += self.encien_val_pay[0]
            self.total_ttc += self.encien_val_pay[1]
            #pour nouvelle class ajoute , on appel comme une class ,;;; on parcourir dans notre liste par indice, aprtier de premier nouvelle article
            for idx_new_article in range(len(self.encien_valeur_table)-1 , len(self.list_article)):
                self.total_ht += self.list_article[idx_new_article].get_info()[4]
                self.total_ttc += self.list_article[idx_new_article].get_info()[5]
            
        else:
            for atricle in self.list_article:
                self.total_ht += atricle.get_info()[4]
                self.total_ttc += atricle.get_info()[5]

        self.total_ht_label.config(text=f"   Total HT :   {self.total_ht } € ")
        self.total_ttc_label.config(text=f"   Total TTC :  {self.total_ttc } €")

        self.modif_net_payer()

    
    
    def modif_net_payer(self, event=None):
        mont_remis = float(self.entr_remise.get()) if (est_nombre(self.entr_remise.get()) ) else "0"
        
        self.net_a_payer_label.config(text=f"  Net à payer  :  { self.total_ttc - mont_remis} €")



    def update_places(self,y):
        """ on vas recalculer les position des tous wedjet qu'existe apres table article,, car ces postiones chnage selon d'ajouter des articles
        on appel chaque wedjit par son tags
        """
        #position des infos paiment 
        self.canv_fact.coords("Total_HT",860, y+70)
        self.canv_fact.coords("Total_TTC", 860, y+95)
        self.canv_fact.coords("remise", 840, y+120)
        self.canv_fact.coords("entr_remise", 900, y +120)
        self.canv_fact.coords("Net", 860, y+145)
        self.canv_fact.coords("etat_fact", 850, y+170)
        self.canv_fact.coords("box_check", 900, y+170)
        self.canv_fact.coords("Mode", 865, y+195)
        self.canv_fact.coords("carte", 780, y +213)
        self.canv_fact.coords("cheque", 850, y +213)
        self.canv_fact.coords("espece", 920, y +213)
        self.canv_fact.coords("date", 800, y+240)
        self.canv_fact.coords("ent_date", 920, y+240)
        
        self.canv_fact.coords("infos", 200, y+70)
        self.canv_fact.coords("banque", 100, y+95)
        self.canv_fact.coords("ent_banque", 230, y+95 )
        self.canv_fact.coords("rib", 100, y+120)
        self.canv_fact.coords("ent_rib", 230, y+120)
        self.canv_fact.coords("iban", 100, y+145)
        self.canv_fact.coords("ent_iban", 230, y+145)
        self.canv_fact.coords("bic", 100, y+170)
        self.canv_fact.coords("ent_bic", 230, y+170)
        self.canv_fact.coords("remarq", 100, y+250)
        self.canv_fact.coords("text_remarq", 10, y+280)
        self.canv_fact.coords("sing", 870, y+380)
        self.canv_fact.coords("ajoute_sing", 950, y+380)
        self.canv_fact.coords("bouton_annule",375, y+500)
        self.canv_fact.coords("bouton_enregs", 500, y+500)


