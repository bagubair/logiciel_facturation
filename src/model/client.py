import os
from consts import DATA_DIR

class Client:
    def __init__(self, numero, nom, prenom, adresse, telephone, mail,BDD):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone
        self.mail = mail
        self.BDD = BDD

    def ajoute_client_auBDD(self):
        requet = f"INSERT INTO client VALUES({self.nom},{self.prenom},{self.adresse},{self.telephone},{self.mail}),"
        self.BDD.connect()
        self.BDD.execute_requete(requet)
        self.BDD.disconnect()



    def afficher_informations(self):
        print("Numéro:", self.numero)
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Adresse:", self.adresse)
        print("Téléphone:", self.telephone)
        print("Mail:", self.mail)

    def modifier_telephone(self, nouveau_telephone):
        self.telephone = nouveau_telephone

    def modifier_mail(self, nouveau_mail):
        self.mail = nouveau_mail
