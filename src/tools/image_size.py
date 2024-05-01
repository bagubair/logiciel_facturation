from PIL import Image, ImageTk


def size_photo(image, x, y):
    lire_photo = Image.open(image)
    image_modf = ImageTk.PhotoImage(
        lire_photo.resize((x, y)))  # on modifie les dimensions de photo pour ce soit sur le bouton

    return image_modf

