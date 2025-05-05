from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def init_riassunto():
    modello = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(modello)
    model = AutoModelForSeq2SeqLM.from_pretrained(modello)
    model.eval()
    return lambda testo: _riassunto(testo, model, tokenizer)

def _riassunto(testo, model, tokenizer):
    with torch.no_grad():
        inputs = tokenizer([testo], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs["input_ids"], max_length=130, min_length=40, num_beams=4)
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
