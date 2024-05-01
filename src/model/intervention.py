class Intervention:
    def __init__(self, type_intervention, date, description, prix, materiaux_utilises):
        self.type_intervention = type_intervention
        self.date = date
        self.description = description
        self.prix = prix
        self.materiaux_utilises = materiaux_utilises

    def afficher_informations(self):
        print("Type d'intervention:", self.type_intervention)
        print("Date:", self.date)
        print("Description:", self.description)
        print("Prix:", self.prix)
        print("Matériaux utilisés:", self.materiaux_utilises)

    def modifier_prix(self, nouveau_prix):
        self.prix = nouveau_prix
