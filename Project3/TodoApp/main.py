from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


# cmd to run the app
# uvicorn main:app --reload


# {
#   "username": "damu1",
#   "email": "dammu@gmail.com",
#   "first_name": "Damodhar",
#   "last_name": "Ar",
#   "password": "1qaz2wsx",
#   "role": "admin"
# }


# curl -X 'POST' \
#   'http://127.0.0.1:8000/auth/token' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/x-www-form-urlencoded' \
#   -d 'grant_type=password&username=damu1&password=1qaz2wsx&scope=admin&client_id=string&client_secret=********'
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkYW11MSIsImlkIjo0LCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3NTc5MTM1NDJ9.m3fOJISui3thQ5bT3s_F_VIDBRFDl6mrGzXKuh7UxVw",
#   "token_type": "bearer"
# }