import os

# Only try to load .env in local dev
if os.getenv("RAILWAY_ENVIRONMENT") is None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

# Now read variables (works locally + Railway)
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
TEST_KEY = os.getenv("TEST_KEY")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
