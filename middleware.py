from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils import validate_jwt_token

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, exclude_paths: list = None):
        super().__init__(app)
        self.exclude_paths = exclude_paths or [
            "/home",
            "/docs",
            "/redoc",
            "/openapi.json",
            "/api/v1/users"
        ]

    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            return await call_next(request)

        # Skip authentication for excluded paths (match by prefix)
        if any(request.url.path.startswith(path) for path in self.exclude_paths):
            return await call_next(request)

        # Check Authorization header
        authorization = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(
                status_code=401,
                content={"status": "error", "message": "Authorization header is required"}
            )

        # Validate token
        if not validate_jwt_token(authorization):
            return JSONResponse(
                status_code=401,
                content={"status": "error", "message": "Invalid or expired token"}
            )

        return await call_next(request)
