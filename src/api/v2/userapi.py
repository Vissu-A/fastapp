from fastapi import APIRouter, status, Depends
from src.schemas.user import UserSchema, UserDisplay
from src.db.database import get_db
from sqlalchemy.orm import Session
from src.utils.user import create_user
from src.models.user import UserModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post(
    path="/create",
    summary="create a new user",
    description="this will create a new user",
    status_code=status.HTTP_201_CREATED,
    response_description="returns newly created user.",
    response_model=UserDisplay
)
def user_create(request: UserSchema, db: Session = Depends(get_db)):
    print(f"Request Data: {request}")
    return create_user(request, db)


@router.get(
    path="/list",
    summary="list of users",
    description="this will list all users",
    status_code=status.HTTP_200_OK,
    response_description="returns list of users.",
    response_model=list[UserDisplay]
)
def user_create(db: Session = Depends(get_db)):
    return db.query(UserModel).all()
