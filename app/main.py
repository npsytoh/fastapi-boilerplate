import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.routers import router
from app.core.config import settings
from app.schemas.info import InfoResponse

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
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


app.include_router(router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.APP_HOST, port=settings.APP_PORT)
