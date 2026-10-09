"""SplitPot API: the starting point.

Run it with:  uvicorn app.main:app --reload
Then open:    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

app = FastAPI(title="SplitPot", version="0.1.0")


@app.get("/")
def home():
    """A friendly hello so you know the server is up."""
    return {"message": "Welcome to SplitPot"}


@app.get("/healthz")
def healthz():
    """Health check. Kubernetes and monitoring tools call this later in the plan."""
    return {"status": "ok"}
