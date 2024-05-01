class Artisan:
    def __init__(self, nom_entreprise, adresse, telephone, mail, identifiant):
        self.nom_entreprise = nom_entreprise
        self.adresse = adresse
        self.telephone = telephone
        self.mail = mail
        self.identifiant = identifiant

    def ajoute_artisant_auBDD(self):
        requet = f"INSERT INTO artisant VALUES({self.nom_entreprise},{self.adresse},{self.telephone},{self.mail}),"
        self.BDD.connect()
        self.BDD.execute_requete(requet)
        self.BDD.disconnect()


    def afficher_informations(self):
        print("Nom de l'entreprise:", self.nom_entreprise)
        print("Adresse:", self.adresse)
        print("Téléphone:", self.telephone)
        print("Mail:", self.mail)
        print("Identifiant:", self.identifiant)

    def modifier_telephone(self, nouveau_telephone):
        self.telephone = nouveau_telephone

    def modifier_mail(self, nouveau_mail):
        self.mail = nouveau_mail



