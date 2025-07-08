from fastapi import APIRouter, Depends, HTTPException
from models.comment import Comment
from db import comments_collection
from datetime import datetime

router = APIRouter()

# Replace with your actual JWT auth dependency
def get_current_user():
    return "user@example.com"

@router.post("/create")
async def create_comment(comment: Comment, current_user: str = Depends(get_current_user)):
    comment.created_by = current_user
    comment.created_at = datetime.utcnow()

    comment_dict = comment.dict()
    if not comment_dict.get("comment_id"):
        comment_dict.pop("comment_id", None)

    result = await comments_collection.insert_one(comment_dict)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create comment")

    return {"message": "Comment created", "id": str(result.inserted_id)}

@router.get("/posts/{post_id}/comments")
async def get_comments(post_id: str):
    cursor = comments_collection.find({"post_id": post_id}).sort("created_at", -1)
    comments = []
    async for doc in cursor:
        doc["comment_id"] = str(doc["_id"])
        doc.pop("_id")
        comments.append(doc)
    return {"data": comments}
