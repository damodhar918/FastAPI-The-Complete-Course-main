from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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