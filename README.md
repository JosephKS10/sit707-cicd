# SIT707 — CI/CD on GCP (HD Task)

A small Flask REST API (a calculator) deployed to Google Cloud Run via
Google Cloud Build, triggered from GitHub on every push to `main`.

## Stack
- **Application:** Python 3.11, Flask 3, gunicorn
- **Tests:** pytest (unit + integration)
- **Container:** Docker
- **CI/CD:** Google Cloud Build (`cloudbuild.yaml`)
- **Registry:** Google Artifact Registry
- **Runtime:** Google Cloud Run (fully managed)
- **Source:** GitHub (push to `main` triggers the pipeline)

## Repo layout
```
.
├── app/
│   ├── __init__.py
│   ├── calculator.py     # business logic (intentional bug for demo)
│   └── main.py           # Flask routes
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_app.py
├── Dockerfile            # container image definition
├── cloudbuild.yaml       # CI/CD pipeline
├── requirements.txt
├── .gcloudignore
└── .gitignore
```

## Local dev
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v              # run tests
python -m app.main     # run server on :8080
curl localhost:8080/add?a=2&b=3
```

## Pipeline flow
1. `git push` to GitHub `main`
2. Cloud Build trigger fires
3. Stage 1: install deps
4. Stage 2: run pytest — pipeline halts here on failure
5. Stage 3: `docker build`
6. Stage 4: push to Artifact Registry
7. Stage 5: `gcloud run deploy`
8. Cloud Run serves the new revision at the public URL
