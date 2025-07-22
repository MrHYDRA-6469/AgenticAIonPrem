# AgenticAIonPrem Chatbot

This repository contains an example of deploying a lightweight Llama-based chatbot using **Azure Functions** written in Python. The function leverages the `TinyLlama` model from Hugging Face for small-scale, on-premise experimentation.

## Structure

- `TinyLlamaFunction/` – Azure Function implementation.
- `host.json` – Azure Functions host configuration.
- `requirements.txt` – Python dependencies.
- `.github/workflows/` – GitHub Actions workflow for deployment.

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

## Deployment with GitHub Actions

1. Create an Azure Function App in your Azure subscription.
2. In the Azure portal, navigate to the function app and download the **publish profile**.
3. In your GitHub repository settings, add a new secret named `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` and paste the contents of the publish profile.
4. Add another secret `AZURE_FUNCTIONAPP_NAME` containing the name of your function app.
5. Push your code to the `main` branch. The included workflow (`.github/workflows/deploy.yml`) installs dependencies and publishes the app using the publish profile.

## Notes

- The TinyLlama model is used as an example. For production, consider hosting the model on dedicated infrastructure or using Azure AI services for better scalability.
- Ensure the model files are available locally or accessible in the environment where the function runs.
