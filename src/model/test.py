from artisant import Artisan
from client import Client
from intervention import Intervention
from facture import Facture
from basse_donnes import BaseDeDonnee


if __name__ == "__main__":
    # Exemple d'utilisation
    artisan1 = Artisan(
        nom_entreprise="Artisanat XYZ",
        adresse="10 Rue des Artisans, 75001 Paris",
        telephone="0123456789",
        mail="contact@artisanatxyz.com",
        identifiant="ART001"
    )

    client1 = Client(
        numero="123",
        nom="Dupont",
        prenom="Jean",
        adresse="10 Rue de la Paix, 75001 Paris",
        telephone="0123456789",
        mail="jean.dupont@example.com"
    )

    intervention1 = Intervention(
        type_intervention="Réparation",
        date="2022-04-08",
        description="Réparation de câblage électrique",
        prix=100,
        materiaux_utilises=["Câbles électriques", "Connecteurs"]
    )

    # Exemple d'utilisation
    facture1 = Facture(
        ref_facture="FAC001",
        date_facture="2022-04-10",
        prix_total=100,
        artisan=artisan1,
        client=client1,
        intervention=intervention1,
        etat_facture="Non payée"  # Par défaut, la facture est définie comme non payée
    )
    
    # Afficher les informations de la facture
    facture1.afficher_facture()

    # Modifier l'état de la facture
    facture1.modifier_etat_facture("Payée")

    print("\nAfficher à nouveau les informations de la facture après modification\n")
    facture1.afficher_facture()