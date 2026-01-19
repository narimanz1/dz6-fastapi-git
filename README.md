# ДЗ 6 — Git / GitHub

Репозиторий создан для домашнего задания по теме Git.

## Содержимое
- `app/main.py` — мини API на FastAPI
- `requirements.txt` — зависимости
- `.gitignore` — исключения для Git

## Как запустить локально
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
После запуска:

GET /health → проверка статуса

GET /echo/{text} → тестовый эндпоинт
