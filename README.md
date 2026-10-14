# Employee Management API
FastAPI + PostgreSQL + psycopg + Docker Compose sample project.

## Start
Ensure Docker Desktop's Linux/WSL engine is running. In this folder run:
`docker compose up -d --build`

Open Swagger UI: http://127.0.0.1:8000/docs
Health check: http://127.0.0.1:8000/health

The API creates the employees table on startup. Ten fictional sample employees are included in `sample_data/employees.json` for reference and are not auto-imported. Settings are read from `.env`; do not commit `.env` or real secrets.

## Tests
Install dependencies with `pip install -r requirements.txt`, then run `pytest`. Health/model validation tests do not need a live database.

## Structure
`app/core` settings; `app/db` database and repository; `app/models` request models; `app/routes` endpoints; `tests` automated tests; `api_contract.md` endpoint contract.
