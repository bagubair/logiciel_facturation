from artisant import Artisan
from client import Client
from intervention import Intervention


class Facture:
    def __init__(self, ref_facture, date_facture, prix_total, artisan, client, intervention, etat_facture="Non payée"):
        self.ref_facture = ref_facture
        self.date_facture = date_facture
        self.prix_total = prix_total
        self.artisan = artisan
        self.client = client
        self.intervention = intervention
        self.etat_facture = etat_facture

    def afficher_facture(self):
        print("Référence de la facture:", self.ref_facture)
        print("Date de la facture:", self.date_facture)
        print("Prix total:", self.prix_total)
        print("État de la facture:", self.etat_facture)

        print("Artisan:")
        self.artisan.afficher_informations()
        
        print("Client:")
        self.client.afficher_informations()

        print("Intervention:")
        self.intervention.afficher_informations()
        

    def modifier_etat_facture(self, nouvel_etat):
        self.etat_facture = nouvel_etat
