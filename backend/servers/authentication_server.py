from fastapi import APIRouter, Depends, FastAPI
from backend.models.user import UserInput
from backend.models.user_login import UserLogin
from backend.services.db_services.user_db.IUserServiceDB import IUserServiceDB
from backend.services.db_services.user_db.UserServiceDB import UserServiceDB
from backend.services.login.ILoginService import ILoginService
from backend.services.login.LoginService import ALGORITHM, SECRET_KEY, LoginService
from backend.services.password.IPasswordService import IPasswordService
from backend.services.password.PasswordService import PasswordService
from backend.services.user.IUserService import IUserService
from backend.services.user.UserService import UserService

password_service: IPasswordService = PasswordService()
user_service_db: IUserServiceDB = UserServiceDB(password_service)
user_service: IUserService = UserService(user_service_db)
login_service: ILoginService = LoginService(password_service,user_service)

router  = APIRouter(prefix="/auth", tags = ["Auth"])
def get_user_service() -> IUserService:
    return user_service

def get_login_manager() -> ILoginService:
    return login_service

@router.get("/health")
def health() :
    return "Okay"

@router.post("/register")
async def add (user : UserInput, user_service : IUserService = Depends(get_user_service)) :
    await user_service.add(user)
    return "Ok"

@router.post("/login")
async def login (user_login_body : UserLogin, login_manager : ILoginService = Depends(get_login_manager)): 
    token = await login_manager.get_token(user_login_body)
    return token