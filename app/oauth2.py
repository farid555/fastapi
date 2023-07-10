from jose import JWTError, jwt
from datetime import datetime, timedelta 


#SECRET_KEY
#Algorithm
#Expriation time

SECRET_KEY = "1e45d521bcb1c5c8ba7ca19c147b39ce2449217b13684bec06cd4ed0d4e23a5b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return  encoded_jwt
    