import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas  # Renommez le module pour éviter les conflits de noms

def canvas_to_pdf(canvas, filename):
    c = pdf_canvas.Canvas(filename, pagesize=letter)  # Utilisez pdf_canvas.Canvas

    # Obtenez les dimensions du canevas
    width, height = canvas.winfo_width(), canvas.winfo_height()

    # Sauvegarder le contenu du canevas dans un fichier PDF
    c.drawString(100, 750, "Contenu du canevas :")
    c.drawString(100, 730, "-" * 30)
    
    # Dessinez le contenu du canevas ligne par ligne
    y = 700  # Position verticale initiale
    for item in canvas.find_all():
        item_type = canvas.type(item)
        if item_type == "window" :
            # Vérifier si c'est un widget Entry
            widget = canvas.itemcget(item, "window")
            if isinstance(widget, tk.Entry):
                x, y = canvas.coords(item)
                entry_text = widget.get()  # Obtenir le texte de l'Entry
                c.drawString(x, height - y, entry_text)
            elif isinstance(widget, tk.Label):
                x, y = canvas.coords(item)
                label_text = widget.cget("text")
                c.drawString(x, height - y, label_text)
            else:
                pass
        else:
            pass

        
    c.save()

# Utilisation de la fonction pour sauvegarder le canevas en PDF
#canvas_to_pdf(self.canv_devis, "contenu_canevas.pdf")
