from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://karthik:ZPCzf9II1kLz3BkC@cluster0.wakry.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "linkedin_insights"

db_client = None

def get_db():
    return db_client[DB_NAME]

async def init_db():
    global db_client
    db_client = AsyncIOMotorClient(MONGO_URI)
