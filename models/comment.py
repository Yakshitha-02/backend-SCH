from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Comment(BaseModel):
    comment_id: Optional[str] = None  # You can map this to MongoDB _id as string if needed
    post_id: str                      # ID of the post this comment belongs to
    content: str                     # The comment text
    created_by: Optional[str] = None  # Usually user email or user ID, set in backend from auth token
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Timestamp when comment was created

    class Config:
        schema_extra = {
            "example": {
                "post_id": "12345",
                "content": "This is a comment!",
                "created_by": "user@example.com",
                "created_at": "2025-07-08T12:00:00Z"
            }
        }
