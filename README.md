# AgenticAIonPrem Chatbot

This repository contains an example of deploying a lightweight Llama-based chatbot using **Azure Functions** written in Python. The function leverages the `TinyLlama` model from Hugging Face for small-scale, on-premise experimentation.

## Structure

- `TinyLlamaFunction/` – Azure Function implementation.
- `host.json` – Azure Functions host configuration.
- `requirements.txt` – Python dependencies.

## Local Development

1. Install dependencies (requires Python 3.8+):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Start the function locally:
   ```bash
   func start
   ```
3. Send a POST request with JSON `{ "prompt": "Hello" }` to `http://localhost:7071/api/TinyLlamaFunction`.

## Notes

- The TinyLlama model is used as an example. For production, consider hosting the model on dedicated infrastructure or using Azure AI services for better scalability.
- Ensure the model files are available locally or accessible in the environment where the function runs.
