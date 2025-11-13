from uuid import uuid4
from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class UserSchema(BaseModel):
    uid: uuid4
    fullname: str = Field(
        description= "Please enter your full name",
        max_length=50
    )
    username: str = Field(max_length=15)
    email: str = Field()
    passcode: str = Field()
    gender: Gender
    dob: date
    is_active: bool = False
    is_admin: bool = False
    dojoin: datetime
    dologin: datetime
