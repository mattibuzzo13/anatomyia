from PIL import Image
import pytesseract

def estrai_testo(percorso_immagine):
    immagine = Image.open(percorso_immagine)
    testo = pytesseract.image_to_string(immagine)
    return testo.strip()
