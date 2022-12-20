import string
from pydantic import EmailStr, constr, validator
from backend.app.schemas import CoreModel, DateTimeModelMixin, IDModelMixin
from typing import Optional

from datetime import datetime, timedelta
from backend.app.core.config import settings


# Add JWT schemas
class JWTMeta(CoreModel):
    iss: str = "sillians.ai"
    aud: str = settings.JWT_AUDIENCE
    iat: float = datetime.timestamp(datetime.now())
    exp: float = datetime.timestamp(
        datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )


class JWTCreds(CoreModel):
    """How we'll identify users"""

    sub: EmailStr
    username: str


class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """

    pass


class AccessToken(CoreModel):
    access_token: str
    token_type: str
