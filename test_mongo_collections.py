import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import json
from bson import json_util

async def main():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB]
    res1 = await db[settings.SERVICE_COLLECTION].find_one()
    res2 = await db[settings.PROFEAAIONAL_COLLECTION].find_one()
    res3 = await db[settings.USERS_COLLECTION].find_one()
    client.close()
    
    with open("mongo_dump.json", "w") as f:
        json.dump({
            "service": json.loads(json_util.dumps(res1)),
            "professional": json.loads(json_util.dumps(res2)),
            "user": json.loads(json_util.dumps(res3))
        }, f, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
