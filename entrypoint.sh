# !/bin/bash

# DB migration 실행
poetry run python -m api.migrate_cloud_db

# uvicorn 서버 실행
poetry run uvicorn api.main:app --host 0.0.0.0