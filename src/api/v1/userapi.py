from fastapi import APIRouter, status, Response

from src.schemas import userschema

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post(
    path="/signup",
    summary="new user",
    description="creating new user",
    status_code=status.HTTP_200_OK,
    response_description="returns newly created user."
)
def user_signup(user: userschema.MyUser) -> dict:
    return {
        "data" : user
    }

@router.get(
    path="/{uid}",
    summary="gets the user by given id",
    description="this shows the user by given id",
    status_code=status.HTTP_200_OK,
    response_description="Gives the user by the id given."
)
def get_current_user(uid: int, response: Response):
    if uid:
        return {
            "Message": f"user with id {uid} is here."
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "Message": f"No user found with given id {uid}"
        }
