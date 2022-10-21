from backend.services.auth.env import env


bind = f'{env.APP_HOST}:{env.APP_PORT}'
workers = 4
worker_class = 'uvicorn.workers.UvicornWorker'
loglevel = 'info'
timeout = 600