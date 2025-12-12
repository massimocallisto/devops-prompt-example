from fastapi import FastAPI
import random

app = FastAPI()

import json


def get_status():
    status_data = {
        "version": "1.0.0",
        "build_date": "2024-01-01T00:00:00Z",  # Fixed ISO date
        "status": "regular",
        "services": []
    }

    status_data["services"].append(add_firma_digitale())
    status_data["services"].append(add_autenticazione())

    return status_data

def add_firma_digitale():
    service = {
        "service": "firma digitale",
        "author": "mario rossi"
    }
    return service

def add_autenticazione():
    service = {
        "service": "autenticazione",
        "author": "luigi verdi"
    }
    return service

@app.get("/status")
async def fetch_status():
    return get_status()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)