# from fastapi import Depends, FastAPI, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# import jwt
# from backend.models.user import UserInput
# from backend.models.user_collection import UserCollection
# from backend.models.user_login import UserLogin
# from backend.services.db_services.user_db.IUserServiceDB import IUserServiceDB
# from backend.services.db_services.user_db.UserServiceDB import UserServiceDB
# from backend.services.login.ILoginService import ILoginService
# from backend.services.login.LoginService import ALGORITHM, SECRET_KEY, LoginService
# from backend.services.password.IPasswordService import IPasswordService
# from backend.services.password.PasswordService import PasswordService
# from backend.services.user.IUserService import IUserService
# from backend.services.user.UserService import UserService
# from jose import JWTError

# password_service: IPasswordService = PasswordService()
# user_service_db: IUserServiceDB = UserServiceDB(password_service)
# user_service: IUserService = UserService(user_service_db)
# login_service: ILoginService = LoginService(password_service,user_service)

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def get_user_service() -> IUserService:
#     return user_service

# def get_login_manager() -> ILoginService:
#     return login_service

# async def get_current_admin(user_service : IUserService = Depends(get_user_service),token = Depends(oauth_scheme)) :
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("username")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return await user_service.get_user(username)
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

# app = FastAPI()

# @app.get("/all")
# async def get_all(user_service : IUserService = Depends(get_user_service)) -> UserCollection:
#     users_service = await user_service.get_all()
#     return UserCollection(Users=users_service)
    
# @app.get("/delete_database")
# async def delete_all(user_service : IUserService = Depends(get_user_service)) -> str:
#     delete_all_data = await user_service.delete_database()
#     return delete_all_data  
