# SplitPot

A small app for splitting shared expenses (rent, groceries, trips), built to learn
Site Reliability Engineering and Forward Deployed Engineering by running it like a
real production service.

Right now it is Day 1: a tiny web server with two endpoints.

## Run it on Windows

Open **PowerShell** in this folder, then:

```powershell
# 1. Create a private Python environment for this project (one time)
python -m venv .venv

# 2. Switch it on (do this every time you open a new terminal)
.venv\Scripts\Activate.ps1

# 3. Install the libraries the app needs (one time)
pip install -r requirements.txt

# 4. Start the server
uvicorn app.main:app --reload
```

If step 2 says "running scripts is disabled", run this once and try again:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Now open these in your browser:

- http://127.0.0.1:8000/ shows the welcome message
- http://127.0.0.1:8000/healthz shows `{"status": "ok"}`
- http://127.0.0.1:8000/docs shows interactive API docs you can click through

Press `Ctrl+C` in the terminal to stop the server.

## Run the tests

```powershell
pytest
```

You should see `2 passed`.

## Project layout

```
app/main.py           the web server
tests/test_health.py  automatic checks that the server answers correctly
requirements.txt      the Python libraries we use
```

## Roadmap

9 phases over 10 weeks: MVP, CI/CD and IaC, Kubernetes, observability and SLOs,
incidents and chaos, scale and disaster recovery, security and cost, a customer
(FDE) engagement, and automation.
