import tkinter as tk

from const import *
from tools.event_entry import effacer_indicatif


class Article():
    def __init__(self,canvas,pos_vertical,nb, parent):
        self.canv_fact = canvas
        self.y = pos_vertical
        self.nb = nb
        print("nb d'article :",self.nb)
        self.parent = parent

        

        self.init_article()
        self.entry_prix.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_prix, "0.00" ))
        self.entry_qnt.bind("<FocusIn>", lambda event: effacer_indicatif(self.entry_qnt, "0" ))

        self.entry_prix.bind("<FocusOut>", self.focus_out_event)
        self.entry_qnt.bind("<FocusOut>", self.focus_out_event)
    def init_article(self): 
        button_suprim = tk.Button(self.canv_fact, width=1, height=1, text="X", command=lambda: self.via_parent())
        self.id_but = self.canv_fact.create_window(20, self.y, anchor="nw", window=button_suprim,tags=f"supprimer_{self.nb}")
 
        self.entry_des = tk.Text(self.canv_fact, bg="white", width=70, height=6)
        self.id_desc = self.canv_fact.create_window(50, self.y, anchor="nw", window=self.entry_des,tags=f"descrip_{self.nb}")
        self.entry_des.insert(tk.END, "Description De L'intervention")

        self.entry_prix = tk.Entry(self.canv_fact, width=10)
        self.id_prix = self.canv_fact.create_window(560, self.y, anchor="nw", window=self.entry_prix,tags=f"prix_{self.nb}")
        self.entry_prix.insert(0,"0.00")

        self.entry_qnt = tk.Entry(self.canv_fact, width=7)
        self.id_qnt = self.canv_fact.create_window(650, self.y, anchor="nw", window=self.entry_qnt,tags=f"qnt_{self.nb}")
        self.entry_qnt.insert(0,"0")

        prix = self.entry_prix.get()
        qnt = self.entry_qnt.get()

        self.total_ht = tk.Label(self.canv_fact, text=f"{self.get_total_ht(prix,qnt)} €",bg=COULEUR_LABEL)
        self.id_ht = self.canv_fact.create_window(740, self.y, anchor="nw", window=self.total_ht,tags=f"tot_ht_{self.nb}")
        
        self.prix_tva = tk.Label(self.canv_fact, text=f"{self.get_TVA(prix,qnt)} €",bg=COULEUR_LABEL)
        self.id_tva = self.canv_fact.create_window(820, self.y, anchor="nw", window=self.prix_tva,tags=f"get_tva_{self.nb}")
        
        self.total_TC = tk.Label(self.canv_fact, text=f"{self.get_TTC(prix,qnt)} €",bg=COULEUR_LABEL)
        self.id_ttc = self.canv_fact.create_window(900, self.y, anchor="nw", window=self.total_TC,tags=f"get_totC_{self.nb}")

    def get_info(self):
        descrip = self.entry_des.get("1.0", "end-1c")
        prix_unit = self.entry_prix.get()
        qnt = self.entry_qnt.get()
        prix_ht = self.get_total_ht(prix_unit,qnt)
        return [descrip, prix_unit, qnt, prix_ht]


    def via_parent(self):
        self.parent.supprime_article(self.nb)

    def supprime(self,nb):
        self.canv_fact.delete(f"supprimer_{nb}")
        self.canv_fact.delete(f"descrip_{nb}")
        self.canv_fact.delete(f"prix_{nb}")
        self.canv_fact.delete(f"qnt_{nb}")
        self.canv_fact.delete(f"tot_ht_{nb}")
        self.canv_fact.delete(f"get_tva_{nb}")
        self.canv_fact.delete(f"get_totC_{nb}")

        return self.y #renvois sa postion pour quand mise a jour les suivant 

    def mise_jour(self,nb, y):
        self.y = y
        print("nb avant mod",self.nb)
        self.canv_fact.coords(f"supprimer_{nb}", 20, y)
        self.canv_fact.coords(f"descrip_{nb}", 50,y )
        self.canv_fact.coords(f"prix_{nb}", 560,y)
        self.canv_fact.coords(f"qnt_{nb}", 650, y)
        self.canv_fact.coords(f"tot_ht_{nb}", 740, y)
        self.canv_fact.coords(f"get_tva_{nb}", 820, y)
        self.canv_fact.coords(f"get_totC_{nb}", 900, y)

    def modif_tags(self,nb,new_nb):
        print("new_nb",new_nb)
        self.canv_fact.itemconfigure(f"supprimer_{nb}", tags=f"supprimer_{new_nb}")
        self.canv_fact.itemconfigure(f"descrip_{nb}", tags=f"descrip_{new_nb}")
        self.canv_fact.itemconfigure(f"prix_{nb}", tags=f"prix_{new_nb}")
        self.canv_fact.itemconfigure(f"qnt_{nb}", tags=f"qnt_{new_nb}")
        self.canv_fact.itemconfigure(f"tot_ht_{nb}", tags=f"tot_ht_{new_nb}")
        self.canv_fact.itemconfigure(f"get_tva_{nb}", tags=f"get_tva_{new_nb}")
        self.canv_fact.itemconfigure(f"get_totC_{nb}", tags=f"get_totC_{new_nb}")
        
    def get_total_ht(self,prix,qnt):
        res = float(prix) * int(qnt)
        
        return res

    def get_TVA(self,prix,qnt):
        ht = self.get_total_ht(prix,qnt)
        res = ht * 0.2
        return res

    def get_TTC(self,prix,qnt):
        ht = self.get_total_ht(prix,qnt)
        tva = self.get_TVA(prix,qnt)
        res = ht + tva
        
        return res

    def focus_out_event(self, event: None):
        # Exécuter le code lorsque l'utilisateur a terminé de saisir des valeurs
        prix = self.entry_prix.get()
        qnt = self.entry_qnt.get()

        ht = self.get_total_ht(prix, qnt)
        tva = self.get_TVA(prix,qnt)
        ttc = self.get_TTC(prix,qnt)

        self.total_ht.config(text=f"{ht} €")
        self.prix_tva.config(text=f"{tva} €")
        self.total_TC.config(text=f"{ttc} €")

##################################################################################################################################""
class TableArticle():
    def __init__(self,canvas,pos_vertical):

        self.canv_fact = canvas
        self.y = pos_vertical

        self.info_table_articles()

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

        tva = tk.Label(self.canv_fact, text="TVA(20%)",bg=COULEUR_LABEL)
        self.canv_fact.create_window(840, 385, anchor="n", window=tva)

        total_ttc = tk.Label(self.canv_fact, text="Total TTC",bg=COULEUR_LABEL)
        self.canv_fact.create_window(920, 385, anchor="n", window=total_ttc)

        ligne_2 = self.canv_fact.create_line(15,415, 990, 415, fill="black")

        self.nb = 0 #pour conter numbre des article
        self.list_article = []
        
        self.ajoute_article()
        
        bouton_ajout = tk.Button(self.canv_fact, text="+",bg="black",fg="white", command=lambda: self.ajoute_article())
        self.canv_fact.create_window(20, self.y, anchor="nw", window=bouton_ajout,tags="ajoute")

        ligne_3 = self.canv_fact.create_line(15,self.y +40 , 990,self.y+40,tags="linge_3", fill="black")
        
        

    
    

    def ajoute_article(self):
        Article(self.canv_fact, self.y, self.nb,self)
        self.list_article.append(Article(self.canv_fact, self.y, self.nb,self))
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
        print("indx",indx)
        new_y = self.list_article[indx].supprime(indx)
        if indx != (len(self.list_article)-1):
            for i in range(indx+1 , len(self.list_article)):
                print("i :", i)
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
        for atricle in self.list_article:
            articles.append(atricle.get_info())
            total_ht += atricle.get_info()[3]

        return [articles, total_ht]

    def update_places(self,y):
        """ on vas recalculer les position des tous wedjet qu'existe apres table article,, car ces postiones chnage selon d'ajouter des articles
        on appel chaque wedjit par son tags
        """
        #position des infos paiment 
        self.canv_fact.coords("Total_HT",800, y+70)
        self.canv_fact.coords("TVA", 800, y+95)
        self.canv_fact.coords("Total_TTC", 800, y+120)
        self.canv_fact.coords("Net", 800, y+145)
        self.canv_fact.coords("Mode", 780, y+170)
        self.canv_fact.coords("date", 780, y+195)
        self.canv_fact.coords("ent_date", 900, y+195)
        self.canv_fact.coords("etat_fact", 800, y+220)
        self.canv_fact.coords("box_check", 860, y+220)
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


