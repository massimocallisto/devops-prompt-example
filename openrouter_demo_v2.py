"""Minimal example of calling the OpenRouter API with structured prompting."""

import os
import sys
from typing import Dict, Any

import requests
from dotenv import load_dotenv


load_dotenv()

OPENROUTER_URL = os.getenv(
    "OPENROUTER_API_URL", "https://openrouter.ai/api/v1/chat/completions"
)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/auto")


SYSTEM_PROMPT = """
Sei un assistente DevOps senior.
Rispondi in modo tecnico, chiaro e pratico.
Quando generi codice o configurazioni, privilegia sicurezza, semplicità e best practice.
Non inventare dettagli non forniti dall'utente.
Se mancano informazioni, dichiara le assunzioni fatte.
"""


def build_prompt(user_input: str) -> str:
    return f"""
CONTESTO:
Stiamo lavorando a un corso DevOps/DevSecOps.
I partecipanti stanno sviluppando microservizi containerizzati,
con pipeline GitHub Actions, Docker e Kubernetes.

ISTRUZIONE:
Rispondi alla richiesta dell'utente producendo un output utile per un team DevOps.

VINCOLI:
- Usa esempi pratici.
- Evidenzia eventuali rischi o assunzioni.
- Se generi codice, rendilo pronto da copiare.
- Mantieni la risposta sintetica.

RICHIESTA UTENTE:
{user_input}
"""


def call_openrouter(user_input: str) -> str:
    """Send user text to OpenRouter and return the model response."""
    if not user_input.strip():
        raise ValueError("User input cannot be empty.")
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY env var must be set.")

    payload: Dict[str, Any] = {
        "model": DEFAULT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": build_prompt(user_input),
            },
        ],
        "temperature": 0.3,
        "max_tokens": 800,
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.getenv("OPENROUTER_HTTP_REFERER", "http://localhost"),
        "X-Title": os.getenv("OPENROUTER_APP_TITLE", "Prompt Lab Demo"),
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected response format: {data}") from exc


def main() -> int:
    user_input = input("Enter a prompt for the LLM: ").strip()

    if not user_input:
        print("No input provided.")
        return 1

    try:
        reply = call_openrouter(user_input)
    except Exception as exc:
        print(f"Error while contacting OpenRouter: {exc}")
        return 1

    print("\nLLM response:\n")
    print(reply)
    return 0


if __name__ == "__main__":
    sys.exit(main())