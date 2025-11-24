import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"],
)

result = client.translation(
    "Меня зовут Вольфганг и я живу в Берлине",
    model="Helsinki-NLP/opus-mt-fr-en",
)