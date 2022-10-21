import uvicorn


from backend.services.auth.env import env


def run():
    uvicorn.run(
        'backend.services.auth.main:web_app',
        host=env.APP_HOST,
        port=env.APP_PORT,
        reload=True
    )


if __name__ == '__main__':
    run()