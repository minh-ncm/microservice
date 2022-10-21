#/bin/bash
export $(cat .env | xargs)
uvicorn --host $APP_HOST --port $APP_PORT --reload backend.services.auth.main:web_app