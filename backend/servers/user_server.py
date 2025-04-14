from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from backend.services.db_services.user_db.IUserServiceDB import IUserServiceDB
from backend.services.db_services.user_db.UserServiceDB import UserServiceDB
from backend.services.db_services.user_property_db.IUserPropertyServiceDB import IUserPropertyServiceDB
from backend.services.db_services.user_property_db.UserPropertyServiceDB import UserPropertyServiceDB
from backend.services.login.ILoginService import ILoginService
from backend.services.login.LoginService import ALGORITHM, SECRET_KEY, LoginService
from backend.services.password.IPasswordService import IPasswordService
from backend.services.password.PasswordService import PasswordService
from backend.services.user.IUserService import IUserService
from backend.services.user.UserService import UserService
from backend.services.user.property.IUserPropertyService import IUserPropertyService
from backend.services.user.property.UserPropertyService import UserPropertyService
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags = ["User"])

password_service: IPasswordService = PasswordService()
user_service_db: IUserServiceDB = UserServiceDB(password_service)
user_service: IUserService = UserService(user_service_db)
user_property_service_db : IUserPropertyServiceDB = UserPropertyServiceDB()
user_property_service : IUserPropertyService = UserPropertyService(user_property_service_db)
login_service: ILoginService = LoginService(password_service,user_service)

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user_service() -> IUserService:
    return user_service

def get_login_manager() -> ILoginService:
    return login_service

def get_user_property_service() -> IUserPropertyService :
    return user_property_service

async def get_current_user(user_service : IUserService = Depends(get_user_service),token : str = Depends(oauth_scheme)) :
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Helo")
        username = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return await user_service.get_user(username)
    except Exception as e:
        raise e



@router.get("/follow")
async def follow_user(to_follow : str,user_property_service : IUserPropertyService = Depends(get_user_property_service),user =  Depends(get_current_user)) -> str:
    print("Follow user")
    print(user["username"])
    await user_property_service.follow(user["username"],to_follow)
    return "Ok"

@router.get("/follow/{to_follow}")
async def follow_user(to_follow : str,user_property_service : IUserPropertyService = Depends(get_user_property_service),user =  Depends(get_current_user)) -> str:
    await user_property_service.follow(user["username"],to_follow)
    return "Ok"

@router.get("/get_me")
async def get_me(username =  Depends(get_current_user)) :
    # username = await get_current_user()
    # if username is None:
    #     raise HTTPException(status_code=401, detail="Invalid token")
    
    return username