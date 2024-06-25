from fastapi import FastAPI
from web_api.routers import api_router

app = FastAPI(title="WebApi")
app.include_router(api_router)
