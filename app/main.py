"""SplitPot API: the starting point.

Run it with:  uvicorn app.main:app --reload
Then open:    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SplitPot", version="0.1.0")


@app.get("/")
def home():
    """A friendly hello so you know the server is up."""
    return {"message": "Welcome to SplitPot"}


@app.get("/healthz")
def healthz():
    """Health check. Kubernetes and monitoring tools call this later in the plan."""
    return {"status": "ok"}
class GroupIn(BaseModel):
    name: str

groups = []

@app.post("/groups")
def create_group(group: GroupIn):
    new_group = {"id": len(groups) + 1, "name": group.name}
    groups.append(new_group)
    return new_group

@app.get("/groups")
def list_groups():
    return groups