# Anatomy Helper

Un'applicazione web per analizzare tavole anatomiche:
- Estrae testo da immagini
- Genera un riassunto schematico
- Crea domande aperte in stile flashcard

## Come eseguirlo

1. Installa le dipendenze:
```bash
cd backend
pip install -r requirements.txt
```

2. Avvia il server
```bash
uvicorn main:app --reload
```

3. Apri ```frontend/index.html``` nel browser.

## Requisiti extra

- Python 3.8+
- Tesseract OCR installato e funzionante

---