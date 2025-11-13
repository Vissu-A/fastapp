from sqlalchemy.exc import IntegrityError
from uuid import uuid4
from sqlalchemy.orm import session
from src.schemas.user import UserSchema
from src.models.user import UserModel
from fastapi import HTTPException

from src.utils.hash import PasscodeHash

def create_user(request: UserSchema, db: session):
    print(f"Creating user with data: {request}")
    new_user = UserModel(
        uid= uuid4(),
        username =  request.username,
        email = request.email,
        passcode = PasscodeHash().encrypt_passcode(request.passcode),
        dob = request.dob,
        gender = request.gender
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
