from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Comment(BaseModel):
    comment_id: Optional[str] = None
    post_id: str
    content: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None

    