import traceback
import cloudinary
import cloudinary.uploader
import os

# Get all required variables
CLOUD_ENV = os.environ.get('CLOUDINARY_CLOUD_NAME')
CLOUD_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
CLOUD_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')

# Print them so you know they're loaded
print("Cloudinary configuration:")
print("Cloud Name:", CLOUD_ENV)
print("API Key:", CLOUD_API_KEY)
print("API Secret:", CLOUD_API_SECRET)

# Configure Cloudinary
cloudinary.config(
    cloud_name=CLOUD_ENV,
    api_key=CLOUD_API_KEY,
    api_secret=CLOUD_API_SECRET,
)

def upload_file_to_cloudinary(file):
    try:
        print("Uploading to Cloudinary...")
        response = cloudinary.uploader.upload(file)
        print("Cloudinary upload response:", response)
        return response['secure_url']
    except Exception as e:
        print("Error uploading file to Cloudinary:")
        traceback.print_exc()
        return None
