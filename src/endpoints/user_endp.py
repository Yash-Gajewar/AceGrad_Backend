from fastapi import HTTPException, APIRouter



# router = APIRouter(
#     prefix="/api/user",
#     tags=["user"],
#     responses={404: {"description": "Not found"}},
# )


# @router.post("/createuser")
# async def post_user(user : User):
#     result = create_user(user.dict())
#     if(result == "duplicate"):
#         return {"SUCCESS":"FALSE", "ITEM":"NULL"}
#     else:
#         return {"SUCCESS":"TRUE"} 

# @router.get("/userexists")
# async def get_user(email :str, password:str):
#     result =  user_exists(email, password)
#     if result:
#         return {"SUCCESS":"TRUE"}
#     else:
#         return {"SUCCESS":"FALSE"} 



       

