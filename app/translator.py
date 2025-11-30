from app.config import HF_TOKEN
import requests



def translate_text(input_text, source, target):

    MODELS = {
        ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
        ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    }

    model_name = MODELS.get((source.lower(), target.lower()))

    if not model_name:
        return {"error": "Language pair not supported"}

    API_URL = f"https://router.huggingface.co/hf-inference/models/{model_name}"
    
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
    }

    payload = {"inputs": input_text}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()