from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
from datetime import datetime
from bson import ObjectId
from typing import Optional, Annotated, List

class Post(BaseModel):
    post_id: Optional[str]
    type: str
    title: str
    content: str
    file_url: Optional[str] = None
    tags: Optional[List[str]] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None

    