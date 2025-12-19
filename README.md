# Prompt Lab

Questo progetto contiene esempi di utilizzo dell'API di OpenRouter per integrare risposte LLM.

## Prerequisiti

- Python 3.8 o superiore
- Un account OpenRouter con una chiave API valida

## Installazione

### 1. Creazione del Virtual Environment

Crea un virtual environment per isolare le dipendenze del progetto:

```bash
python3 -m venv venv
```

Attiva il virtual environment:

- Su macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

- Su Windows:
  ```bash
  venv\Scripts\activate
  ```

### 2. Installazione delle Dipendenze

Installa le dipendenze richieste:

```bash
pip install -r requirements.txt
```

## Configurazione

Crea un file `.env` nella directory principale del progetto con le seguenti variabili d'ambiente:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=openrouter/auto  # Modello predefinito (opzionale)
OPENROUTER_HTTP_REFERER=http://localhost  # Referer per rate limiting (opzionale)
OPENROUTER_APP_TITLE=Prompt Lab Demo  # Titolo dell'app (opzionale)
```

Sostituisci `your_openrouter_api_key_here` con la tua chiave API di OpenRouter.

## Esecuzione

### Esempio con openrouter_demo.py

Questo script permette di interagire con l'API di OpenRouter tramite input da terminale.

```bash
python openrouter_demo.py
```

Inserisci un prompt quando richiesto, e lo script restituirà la risposta del modello LLM.

### Esempio con main.py

Se hai un server FastAPI in esecuzione:

```bash
python main.py
```

Oppure usando uvicorn direttamente:

```bash
uvicorn main:app --reload
```

## Note

- Assicurati che il virtual environment sia attivato prima di eseguire qualsiasi script.
- La chiave API di OpenRouter è necessaria per autenticare le richieste.
- Puoi personalizzare il modello e altre impostazioni tramite variabili d'ambiente nel file `.env`.