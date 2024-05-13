from pylatex import Document, Section, Command, Tabular, Package, MiniPage, Figure
from const import *


def convert_pdf(id_utilisateur, info_facture, info_entreprise, info_client, table_articles, infos_supplem, devis=None):

    if(devis):
        title = "Devis"
        
    else:
        title = "Facture"
        info_banqu = infos_supplem[3]

    num_title = info_facture[0]
    logo = info_entreprise[5]
    info_pay = infos_supplem[0]
    remarque = infos_supplem[1]
    singature = infos_supplem[2]

    # Créer un document LaTeX
    doc = Document()

    # Ajouter des packages pour la mise en page
    doc.packages.append(Package('geometry', options=['top=0.5cm', 'bottom=0.5cm', 'left=0.5cm', 'right=0.5cm']))

    # Ajouter les informations de la facture
    
    doc.append(Command('begin', 'Center'))
    doc.append(f"{title} \n")
    doc.append(Command('end', 'Center'))


    if ( logo):
        with doc.create(MiniPage(width=r'0.5\textwidth')):
            doc.append(Command('begin', 'flushleft'))
            with doc.create(Figure(position='h!')) as image:
                image.add_image(logo, width='200px')
            
            doc.append(Command('end', 'flushleft'))


        with doc.create(MiniPage(width=r'0.5\textwidth')):
            doc.append(Command('begin', 'flushright'))
            doc.append(f"N° {title} : {info_facture[0]}\n")
            doc.append(f"Date {title} : {info_facture[1]}\n")
            doc.append(f"Ref Client : {info_facture[2]}\n")
            doc.append(Command('end', 'flushright'))

    else:
        with doc.create(Section('', numbering=False)):
            doc.append(f"N° {title} : {info_facture[0]}\n")
            doc.append(f"Date {title} : {info_facture[1]}\n")
            doc.append(f"Ref Client : {info_facture[2]}\n")
            doc.append('\n')
            doc.append('\n')
        with doc.create(Section('', numbering=False)):
            doc.append('De \n')
            doc.append(f'Nom Entrprise : {info_entreprise[0]}\n')
            doc.append(f'Adresse : {info_entreprise[1]}\n')
            doc.append(f'Mail : {info_entreprise[2]}\n')
            doc.append(f'Tél. Fixe : {info_entreprise[3]}\n')
            doc.append(f'N° SIREN/SIRET : {info_entreprise[4]}\n')
            doc.append('\n')
            doc.append('\n')
        with doc.create(Section('', numbering=False)):
            doc.append('Adresse De Facturation : \n')
            doc.append(f'Nom Client  : {info_client[0]}\n')
            doc.append(f'Prénom Client : {info_client[1]}\n')
            doc.append(f'Adresse : {info_client[2]}\n')
            doc.append(f'Tél. Fixe : {info_client[3]}\n')
            doc.append(f'Tél Mobile : {info_client[4]}\n')
            doc.append(Command('end', 'flushleft'))


        
  
    # Ajouter le tableau des articles
    with doc.create(Section('', numbering=False)):
        with doc.create(Tabular('|c|c|c|c|c|c|')) as table:
            table.add_hline()
            table.add_row(('Intervention', 'Prix unitaire', 'Quantité', 'Total HT', 'TVA %', 'Total TTC'))
            table.add_hline()
            for article in table_articles:
                table.add_row(article )
            table.add_hline()

    if (devis):
        with doc.create(Section('', numbering=False)):
            doc.append(Command('begin', 'flushright'))
            doc.append('\n')
            doc.append('\n')
            doc.append(f'Total HT : {info_pay[0]}\n')
            doc.append(f'Total TTC : {info_pay[1]}\n')
            doc.append('\n')
            doc.append('\n')
            doc.append(Command('end', 'flushright'))
        
            
        if(len(remarque) > 0):
            with doc.create(Section('', numbering=False)):
                doc.append(f"Remarque : \n")
                doc.append(f"{remarque}\n")
            
            doc.append('\n')
        
            
    else:
        #dans cas une facture ,, ici on ajoute les infos de banque 
        with doc.create(Section('', numbering=False)):
            doc.append(Command('begin', 'flushleft'))
            
            doc.append('\n')
            doc.append('\n')
            doc.append(f"Informations Bancaires : \n")
            doc.append(f'Nom Banque : { info_banqu[0]}\n')
            doc.append(f'RIB : { info_banqu[1]}\n')
            doc.append(f'IBAN : { info_banqu[2]}\n')
            doc.append(f'BIC : { info_banqu[3]}\n')
        
            doc.append('\n')
            doc.append(Command('end', 'flushleft'))


        with doc.create(Section('', numbering=False)):
            doc.append(Command('begin', 'flushright'))
            doc.append('\n')
            doc.append(f'Total HT : {info_pay[0]}\n')
            doc.append(f'Total TTC : {info_pay[1]}\n')
            doc.append(f'Remise : {info_pay[2]}\n')
            doc.append(f'Solde Dû : {info_pay[4]}\n')
            doc.append(f'Mode de paiement  : {info_pay[5]}\n')
            doc.append(f"Date d'échange : {info_pay[6]}\n")
            doc.append('\n')
            doc.append(Command('end', 'flushright'))

        if(len(remarque) > 0):
            with doc.create(Section('', numbering=False)):
                doc.append(f"Remarque : \n")
                doc.append(f"{remarque}\n")
            
                doc.append('\n')

    if (singature == 1):
        with doc.create(Section('', numbering=False)):
            with doc.create(Figure(position='h!')) as image:
                image_singe = os.path.join(DATA_DIR, f"signature_{id_utilisateur}.png")
                image.add_image(image_singe, width='200px')


    # Générer le PDF
    doc.generate_pdf(f"DATA/{num_title}_ID_{id_utilisateur}.pdf", clean_tex=True)
