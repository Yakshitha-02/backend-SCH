import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_router import router as user_router
from routes.post_router import router as post_router
from routes.comment_router import router as comment_router
from middleware import AuthMiddleware
from env import TEST_KEY

app = FastAPI(
    title="Student Collaboration App",
    description="A single app for students to collaborate",
    version="1.0.0"
)

# ✅ CORSMiddleware (first)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://frontendsch.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ AuthMiddleware (second)
app.add_middleware(AuthMiddleware)

# ✅ Routers
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(post_router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(comment_router, prefix="/api/v1/comments", tags=["comments"])

@app.get("/home", response_model=dict)
async def home():
    return {"message": TEST_KEY}
