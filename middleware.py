from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils import validate_jwt_token

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, exclude_paths: list = None):
        super().__init__(app)
        # Paths that don't require authentication
        self.exclude_paths = exclude_paths or [
            "/home",
            "/docs",
            "/redoc", 
            "/openapi.json",
            "/api/v1/users/sign-up",
            "/api/v1/users/login",
            "/api/v1/posts/"
        ]
    
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            return await call_next(request)
        # Skip authentication for excluded paths
        if request.url.path in self.exclude_paths:
            return await call_next(request)
        
        # Check for Authorization header
        authorization = request.headers.get("Authorization")
        
        if not authorization:
            return JSONResponse(
                status_code=401,
                content={
                    "status": "error",
                    "message": "Authorization header is required"
                }
            )
        
        # Validate JWT token
        if not validate_jwt_token(authorization):
            return JSONResponse(
                status_code=401,
                content={
                    "status": "error",
                    "message": "Invalid or expired token"
                }
            )
        
        # Add user info to request state if needed
        # You can decode the token here and add user data to request.state
        
        response = await call_next(request)
        return response


