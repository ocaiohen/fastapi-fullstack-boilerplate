from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import api_router
# from core.config import settings


def create_app() -> FastAPI:
    disable_docs = False
    # disable_docs = settings.ENVIRONMENT == "production"

    app = FastAPI(
        title="Your app name",
        description='Your app description',

        # para desativar docs (em produção)
        docs_url=None if disable_docs else "/docs",
        redoc_url=None if disable_docs else "/redoc",
        openapi_url=None if disable_docs else "/openapi.json"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.middleware("http")(token_bucket_middleware)

    app.include_router(api_router, prefix="/api")

    return app

app = create_app()

@app.get('/')
def hello_World():
    return {"message": "Ê lasquêra"}