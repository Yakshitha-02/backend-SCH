# import bcrypt

# def get_hashed_password(password: str) -> str:
#     bytes = password.encode('utf-8')
#     salt = bcrypt.gensalt(rounds=12, prefix=b"2b")
#     hashed_password = bcrypt.hashpw(bytes, salt)
#     return hashed_password.decode('utf-8')

# def check_password(hashed_password: str, password: str) -> bool:
#     return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# result = get_hashed_password("password123")

import jwt
from datetime import datetime, timedelta

def create_jwt_token(data: dict) -> str:
    payload = {
        "email": data.get("email"),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, "STUDENT_COLLABORATION_APP_KEY", algorithm="HS256")
    return token


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, "STUDENT_COLLABORATION_APP_KEY", algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
    

print(create_jwt_token({"email": "user.a@mail.com"}))
