from fastapi import FastAPI
from backend.models.user import UserInput
from backend.models.user_collection import UserCollection
from backend.models.user_login import UserLogin
from backend.services.login_managment import LoginService
from backend.services.user_service import UserService

app = FastAPI()

@app.get("/health")
def health() :
    return "Okay"

@app.post("/register")
async def add (user : UserInput) :
    user_service = UserService()
    await user_service.add(user)
    return "Ok"

@app.post("/login")
async def login (user_login_body : UserLogin) :
    login_manager = LoginService()
    token = await login_manager.get_token(user_login_body)
    return token
    
@app.get("/all")
async def get_all():
    user_service = UserService()
    users_service = await user_service.get_all()
    return UserCollection(Users=users_service)
    
@app.get("/delete_database")
async def delete_all():
    user_service = UserService()
    delete_all_data = await user_service.delete_database()
    return delete_all_data  

@app.get("/get_current_user") 
def get_current_user():
    user_service = UserService()
    current_user = user_service.get_current_user()
    return current_user