from fastapi import FastAPI, Depends
from database import init_db
from routes import page_router
import uvicorn

app = FastAPI(title="LinkedIn Insights Microservice")

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(page_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)