from fastapi import APIRouter

# Creating FastAPI application instance
api: APIRouter = APIRouter(prefix="", tags=["Users"])


# Returns information of currently logged-in user
@api.get("/users/me")
def home() -> dict:
    return {
        "first_name": "Thomas",
        "last_name": "Anderson",
        "display_name": "Thomas Anderson",
        "username": "neo",
        "email": "neo@thematrix.com",
    }
