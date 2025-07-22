import logging
import azure.functions as func
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load TinyLlama model. This is a lightweight Llama-architecture model that is small enough
# for demonstration purposes. On real Azure Functions you might prefer to load this in a
# more efficient way or use the Azure AI deployment services.
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v0.3"  # This model name assumes you've downloaded it.

# Singleton pattern to avoid reloading the model on every function invocation
model = None
tokenizer = None

def load_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        model.to("cpu")  # running on CPU for light-weight environment
    return model, tokenizer

def generate_response(prompt: str) -> str:
    model, tokenizer = load_model()
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Llama chat function processed a request.")

    try:
        req_body = req.get_json()
    except ValueError:
        req_body = {}

    prompt = req_body.get('prompt')
    if not prompt:
        return func.HttpResponse(
            "Please pass a prompt in the request body",
            status_code=400
        )

    response_text = generate_response(prompt)

    return func.HttpResponse(response_text)
