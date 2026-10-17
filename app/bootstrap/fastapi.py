from typing import Annotated

from fastapi import FastAPI, Query, status
from fastapi.responses import JSONResponse

from app.api.v1.routers.home import api as user_router

# Creating FastAPI application instance
api: FastAPI = FastAPI(title="Python Application Reference", tags=["Default"])


# Default endpoint
@api.get("/", status_code=status.HTTP_200_OK)
def index(name: Annotated[str | None, Query(description="Name of user calling this API")] = "World") -> dict:
    return {"message": f"Hello, {name}!!!"}


# Application health endpoint
api_version_prefix = "/api/v1"


@api.get(
    f"{api_version_prefix}/health",
    status_code=status.HTTP_200_OK,
    include_in_schema=True,
)
def home() -> JSONResponse:
    return JSONResponse({"status": "ok"})


api.include_router(user_router, prefix=api_version_prefix)
