from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def init_domande():
    modello = "iarfmoose/t5-base-question-generator"
    tokenizer = AutoTokenizer.from_pretrained(modello)
    model = AutoModelForSeq2SeqLM.from_pretrained(modello)
    model.eval()
    return lambda testo: _genera_domande(testo, model, tokenizer)

def _genera_domande(testo, model, tokenizer):
    prompt = f"generate questions: {testo}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(inputs["input_ids"], max_length=256, num_beams=4)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
