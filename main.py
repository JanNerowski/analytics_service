import sys
from fastapi import FastAPI

app = FastAPI(title="Local Business Finder")

@app.get("/")
def read_root():
    return {
        "service": "Local Business Finder",
        "status": "ready",
        "python_version": sys.version,
    }

@app.get("/search")
def search_business(city: str, category: str):
    return {
        "message": f"Searching for '{category}' in {city}...",
        "results": [],
    }