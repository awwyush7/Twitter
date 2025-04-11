from fastapi import Depends, FastAPI
from backend.models.user import UserInput
from backend.models.user_collection import UserCollection
from backend.models.user_login import UserLogin
from backend.services.login_managment import LoginService
from backend.services.user_service import UserService

common_user_service = UserService()
common_login_service = LoginService()

def get_user_service() -> UserService:
    return common_user_service

def get_login_manager() -> LoginService:
    return common_login_service

app = FastAPI()

@app.get("/health")
def health() :
    return "Okay"

@app.post("/register")
async def add (user : UserInput, user_service = Depends(get_user_service)) :
    await user_service.add(user)
    return "Ok"

@app.post("/login")
async def login (user_login_body : UserLogin, login_manager = Depends(get_login_manager)): 
    token = await login_manager.get_token(user_login_body)
    return token
    
@app.get("/all")
async def get_all(user_service = Depends(get_user_service)) -> UserCollection:
    users_service = await user_service.get_all()
    return UserCollection(Users=users_service)
    
@app.get("/delete_database")
async def delete_all(user_service = Depends(get_user_service)) -> str:
    delete_all_data = await user_service.delete_database()
    return delete_all_data  

@app.get("/get_current_user") 
def get_current_user(user_service = Depends(get_user_service)) -> UserInput:
    current_user = user_service.get_current_user()
    return current_user