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


## Parameter metadata
# parameter_metadata is the additional information about the parameters will be added using metadata. this information is useful for documentation purpose.
# if our parameter is path parameter then we can add metadata using Path function from fastapi.
# if our parameter is query parameter then we can add metadata using Query function from fastapi.
# if our parameter is request body parameter then we can add metadata using Body function from fastapi.
from fastapi import Path, Query, Body

@router.get(
    path="/info/{username}",
    summary="get user info by username",
    description="this api gives the user info by username",
    status_code=status.HTTP_200_OK,
    response_description="Gives the user info by username."
)
def get_user_info(
    username: str = Path(
        title="username",  # Title of the parameter
        description="name ofthe user", # Description of the parameter
        alias="user-name", # Alias for the parameter
        deprecated=False # Mark the parameter as deprecated
        )
) -> dict:
    return {
        "Message": f"user info for {username}"
    }

## Validators
# we can also add validators to the parameters using metadata.
# string validators: max_length, min_length and regex
# number validators: gt, ge, lt, le

@router.get(
    path="/search/",
    summary="search users by age",
    description="this api searches users by age",
    status_code=status.HTTP_200_OK,
    response_description="Gives the list of users filtered by age."
)
def search_users(
    uage: int = Query(
        #default=18, # pssing default value. if we pass default value then the parameter becomes optional.
        default = Ellipsis, # making the parameter required.
        ge=18, # greater than or equal to 18
        le=100 # less than or equal to 100
    )
) -> dict:
    return {
        "Message": f"users with age {uage} found."
    }

@router.get(
    path="/search/by",
    summary="search users by name",
    description="this api searches users by name",
    status_code=status.HTTP_200_OK,
    response_description="Gives the list of users filtered by name."
)
def search_users(
    name: str = Query(
        default = ..., # making the parameter required. short hand to Ellipsis
        min_length=3, # minimum length of 3
        max_length=5, # maximum lenght of charecters can be passed
        regex="^[a-z\s]*$" # only lowercase letters and spaces are allowed, we can use regex for complex or customized validations. This regex argument usesd for the parameter of type string.
    )
) -> dict:
    return {
        "Message": f"users with name {name} found."
    }

## Multple values to single parameter.
# Multiple values are supported only for query parameters. 
# we can pass multiple values to single query parameter using list type hinting.

from typing import List

@router.get(
    path="/serach/nicknames",
    summary="search by nickname",
    description="this will serach the user by given list of nick names.",
    status_code=status.HTTP_200_OK,
    response_description="Give the user matched with given list of nick names"
)
def search_by_nickname(
    nick_names: List[str] = Query(
        default=...,
        title="nickname",
        description="user nick names",
        alias="nick-names-list",
        deprecated=False,
        min_length=2, # minimum 2 nick names are required
        max_length=5  # maximum 5 nick names can be passed
    )
) -> dict:
    return {
        "Message": f"Here is the list of users macthed with give nick names: {nick_names}"
    }


