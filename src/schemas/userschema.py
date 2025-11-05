from uuid import uuid4
from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class MyUser(BaseModel):
    uid: uuid4
    username: str
    email: str
    dob: date
    gender: Optional[Gender] = None
    is_active: bool = False
    is_admin: bool = False
