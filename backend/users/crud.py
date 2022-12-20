from .schemas import UserPasswordUpdate, UserCreate, UserInDB
from backend.users import auth_service
from .models import User, db
from backend.app.core.config import settings


async def create_user(new_user: UserCreate) -> UserInDB:
    # This is a UserPasswordUpdate
    new_password = auth_service.create_salt_and_hashed_password(
        plaintext_password=new_user.password
    )
    # Next we extend our UserCreate schema here
    new_user_params = new_user.copy(update=new_password.dict())
    # Updated and extended UserCreate schema was passed to UserInDB
    new_user_updated = UserInDB(**new_user_params.dict())
    # Just printing the result
    print(new_user_updated)

    # Here we are openning one time connection
    async with db.with_bind(settings.DATABASE_URI) as engine:
        # Database model User creation happens here
        created_user = await User.create(**new_user_updated.dict())

    # And now we nicely return from_orm with UserInDB
    return UserInDB.from_orm(created_user)


async def get_user_by_username(user_name: str) -> UserInDB:
    async with db.with_bind(settings.DATABASE_URI) as engine:
        found_user = await User.query.where(User.username == user_name).gino.first()

    return UserInDB.from_orm(found_user)
