from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from backend.users.schemas import (
    UserBase,
    UserCreate,
    UserInDB,
    UserLogin,
    UserPublic,
    UserUpdate,
    UserPasswordUpdate,
)
from backend.users import auth_service
from backend.users.crud import get_user_by_username
from backend.users.token import AccessToken

from ..crud import get_user_by_username

router = APIRouter()


@router.post(
    "/create",
    tags=["user registration"],
    description="Register the User",
    response_model=UserPublic,
)
async def user_create(user: UserCreate) -> UserInDB:
    from ..crud import create_user

    return await create_user(user)


@router.post(
    "/login",
    tags=["user login"],
    description="Log in the User",
    response_model=UserPublic,
)
async def user_login(user: UserLogin) -> UserPublic:

    found_user = await get_user_by_username(user_name=user.username)
    if auth_service.verify_password(
        password=user.password, salt=found_user.salt, hashed_pw=found_user.password
    ):
        # If the provided password is valid one then we are going to create an access token
        token = auth_service.create_access_token_for_user(user=found_user)
        access_token = AccessToken(access_token=token, token_type="bearer")
        return UserPublic(**found_user.dict(), access_token=access_token)
