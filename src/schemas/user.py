import uuid
from enum import Enum
from datetime import datetime, date
from pydantic import BaseModel, Field

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class UserSchema(BaseModel):
    # dojoin : datetime
    # dologin : datetime

    # # Role identity fields
    # is_active : bool
    # is_admin : bool

    # user input fields
    username : str
    email : str
    passcode : str
    dob : date
    gender : Gender

class UserDisplay(BaseModel):
    uid : uuid.UUID
    username : str
    email : str
    dob: date
    gender : Gender
    class config:
        orm_mode = True,
