from fastapi import FastAPI
from .routes import main_router


app = FastAPI(
    title="NewX",
    version="0.1.0",
    description="NewX is a posting app",
)

app.include_router(main_router)