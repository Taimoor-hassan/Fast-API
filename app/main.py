from fastapi import FastAPI
from app.routs import user


def create_application():
    application = FastAPI()
    application.include_router(user.user_route)
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, I am Describly. Awesome - Your setrup is done & working."}