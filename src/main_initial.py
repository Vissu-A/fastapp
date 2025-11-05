# from fastapi import FastAPI, status, Response

# app =  FastAPI()

# @app.get("/")
# def home():
#     return {"mesage": "Hello World!"}


# ## Path parameters -> these are parameters passed in the URL path.
# @app.get("/{userid}")
# def greet_user(userid):
#     return {
#         "message": f"Hello {userid}!"
#     }

# ## type hints or type validation for path parameters. 
# # in the above example "userid" path parameter will accept any type of value.
# # But we want only integer to be passed to "userid" path parameter.
# # we want to ensure that only integer values are accepted for the given path parameter.
# # we can do this by using python type hints.
# @app.get("/greet/{userid}")
# def greet_user_str(userid: int):
#     return{
#         "message": f"Hello {userid} from greet user str"
#     }

# ## pre-defined list of values for path parameters.
# # we want that only certain values are accepted for a path parameter. otherthan these values shouldn't be accepted.
# # we can define a class by inheriting the Enum class in enum module.
# from enum import Enum
# # Creating our own pre-defined values class.
# # our class must inherit from Enum calss from enum module
# # our class must inherit from the data type class to which our values belongs. In the below example our values are strings so, we should inherit from "str" datatype class.

# class UserType(str, Enum):
#     admin = "admin"
#     sudo = "sudo"
#     client = "client"
#     basic = "basic"

# @app.get('/greet/{uid}/{utype}')
# def greet_user_type(uid: int, utype: UserType) -> dict:
#     return {
#         "Message": f"Hello user! your id and user type are: {uid} - {utype}"
#     }

# ## Query parameters
# # Query parameters starts after completing the path parameters.
# # Query parameters are separated from path parameters using question mark symbol (?).
# # We can use/pass multple query parameters.
# # Multiple Query parameters are separated by AND symbol (&)
# # Function's paramaeters which are not part of the path parameters are called/represented as query parameters.

# @app.get('/user/list')
# def list_user(utype: UserType) -> dict:
#     return {
#         "Message": f"Here is the list of all {utype} users."
#     }
# # Here, function's argument "utype" in not part of the URLPath, so it will be treated as Query parameter.
# # Query parameter "utype" is the type of our pre-defined enum values class "UserType"
# # Query parameter "utype" is a mandatory parameter, always we should pass the value to it, otherwise will get "field required" error.

# # -> Default values to query parameters
# # We want that it should return list of basic users always if no user type given/specified in the Query parameter.
# @app.get("/user/li")
# def li_user(utype: UserType = "basic") -> dict:
#     return {
#         "Message": f"Here is the list of all users with type {utype}"
#     }

# # -> Marking query parameter optional.
# # We want to make the query parameter optional.
# from typing import Optional
# @app.get("/list/user")
# def get_user_list(utype: Optional[UserType] = None) -> dict:
#     return {
#         "Message": f"Here is the user list for user type: {utype}"
#     }

# ## Status codes
# # We can specify the status code for any endpoint using "status_code" parameter of the path operation decorator.
# # status_code paramaeter accepts the status code values from "status" module of fastapi package and it's the default status code returned by that endpoint.

# @app.get('/user/info', status_code=status.HTTP_200_OK)
# def user_info(uid: int) -> dict:
#     return {
#         "Message": f"Here is the info for user with id: {uid}"
#     }

# # We can changes the status code as per the business logic using "Response" object from fastapi package.

# @app.get("/user/delete", status_code = status.HTTP_200_OK)
# def del_user(response: Response, uid: Optional[int] = None) -> dict:
#     if uid:
#         return {
#             "Message": f"User with id {uid} deleted successfully."
#         }
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {
#             "Message": f"No user found with id {uid}."
#         }
    
# ## Tags
# # tags are used to group the endpoints in the automatic API documentation.
# # we can specify the tags for any endpoint using "tags" parameter of the path operation decorator
# # tags parameter accepts a list of strings.
# # one endpoint can be part of multiple tag groups.
# # By default, all the endpoints are part of "default" tag group.
# @app.get(path = "/user/details", status_code=status.HTTP_200_OK, tags = ['user'])
# def user_details(response: Response, uid: Optional[int] = None) -> dict:
#     if uid:
#         return {
#             "Message": f"Here are the details for user with id {uid}."
#         }
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {
#             "Message": f"No user found with id {uid}."
#         }

# ## Adding summary and description to endpoints
# # we can add summary and description to any endpoint using "summary" and "description" parameters.
# # By default, FastAPI generates a summary for each endpoint using the function name. If we want to override the default summary, we can use the "summary" parameter.
# # By default, FastAPI doesn't add any description to the endpoint. If we want to add a description, we can use the "description" parameter.
# # If the function having the doc string defined, then FastAPI uses that doc string as the description of the endpoint. If we can override it using the "description" parameter.
# @app.get(
#     path = "/user/profile",
#     summary = "get user profile",
#     description = "gives the complete information of a user.",
#     tags = ['user'],
#     status_code = status.HTTP_200_OK
#     )
# def get_user_profile(response: Response, uid: Optional[int] = None) -> dict:
#     if uid:
#         return {
#             "Message": f"Here is the profile for user with id {uid}."
#         }
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {
#             "Message": f"No user found with id {uid}."
#         }

# ## Adding response description to endpoints
# # we can add response description to any endpoint using "response_description" parameter of the path operation
# @app.get(
#     path = "/emi/li",
#     summary = "list of emis",
#     description = "this endpoint lists all emis available.",
#     tags = ['finance-debt'],
#     status_code = status.HTTP_200_OK,
#     response_description = "Thsi is the list of all available emis."
# )
# def get_emi_li() -> dict:
#     return {
#         "Message": "Here is the list of all available emis."
#     }
