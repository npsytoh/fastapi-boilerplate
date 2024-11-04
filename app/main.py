import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

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


@app.get("/", tags=["info"])
async def get_info() -> dict[str, str]:
    return {"title": settings.TITLE, "version": settings.VERSION}


if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.APP_HOST, port=settings.APP_PORT)
