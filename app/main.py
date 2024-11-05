import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import users
from app.schemas.info import InfoResponse

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.TITLE,
    version=settings.VERSION,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"], response_model=InfoResponse)
async def get_info() -> dict[str, str]:
    return {"title": settings.TITLE, "version": settings.VERSION}


app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.APP_HOST, port=settings.APP_PORT)
