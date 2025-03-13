from fastapi import APIRouter, Depends
from database import get_db
from scraper import scrape_linkedin_page
from models import Page
from typing import Optional

page_router = APIRouter()


@page_router.get("/page/{page_id}", response_model=Page)
async def get_page_details(page_id: str, db=Depends(get_db)):
    page = await db.pages.find_one({"page_id": page_id}, {"_id": 0})  # Exclude MongoDB _id field
    if not page:
        scraped_data = scrape_linkedin_page(page_id)
        if scraped_data:
            await db.pages.insert_one(scraped_data)
            return scraped_data
        return {"error": "Page not found"}
    return page


@page_router.get("/page/{page_id}/posts")
async def get_page_posts(page_id: str, limit: int = 10, offset: int = 0, db=Depends(get_db)):
    page = await db.pages.find_one({"page_id": page_id}, {"_id": 0, "posts": 1})  # Fetch only posts
    if not page or "posts" not in page:
        return {"error": "Page not found or no posts available"}
    
    posts = page.get("posts", [])
    return posts[offset:offset+limit]


@page_router.get("/pages")
async def get_pages(
    followers_min: int = 0,
    followers_max: int = 1_000_000,
    industry: Optional[str] = None,
    name: Optional[str] = None,
    limit: int = 50,  # Default limit to avoid overloading
    db=Depends(get_db)
):
    query = {"followers": {"$gte": followers_min, "$lte": followers_max}}
    
    if industry:
        query["industry"] = industry
    if name:
        query["name"] = {"$regex": name, "$options": "i"}  # Case-insensitive search
    
    pages = await db.pages.find(query, {"_id": 0}).limit(limit).to_list(limit)
    return pages
