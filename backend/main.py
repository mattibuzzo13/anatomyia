from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ocr_utils import estrai_testo
from summarizer import init_riassunto
from questions import init_domande
import shutil
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

riassunto_fn = init_riassunto()
domande_fn = init_domande()

@app.post("/analizza/")
async def analizza(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    path_locale = f"temp/{file.filename}"
    with open(path_locale, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    testo = estrai_testo(path_locale)
    if not testo:
        return {"errore": "Testo non rilevato"}

    return {
        "riassunto": riassunto_fn(testo),
        "domande": domande_fn(testo)
    }
