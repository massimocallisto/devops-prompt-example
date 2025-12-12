"""Minimal example of calling the OpenRouter API to integrate an LLM response."""

import os
import sys
from typing import Dict, Any

import requests
from dotenv import load_dotenv


# Load .env once at import time so env vars are available for the rest of the module.
load_dotenv()

# Configure defaults via env vars so the script can run in different environments.
OPENROUTER_URL = os.getenv(
    "OPENROUTER_API_URL", "https://openrouter.ai/api/v1/chat/completions"
)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/auto")


def call_openrouter(user_input: str) -> str:
    """Send user text to OpenRouter and return the model response."""
    if not user_input.strip():
        raise ValueError("User input cannot be empty.")
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY env var must be set.")

    payload: Dict[str, Any] = {
        "model": DEFAULT_MODEL,
        "messages": [{"role": "user", "content": user_input}],
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # OpenRouter recommends sending a referer/title for rate-limit friendliness.
        "HTTP-Referer": os.getenv("OPENROUTER_HTTP_REFERER", "http://localhost"),
        "X-Title": os.getenv("OPENROUTER_APP_TITLE", "Prompt Lab Demo"),
    }

    response = requests.post(
        OPENROUTER_URL, headers=headers, json=payload, timeout=30
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
