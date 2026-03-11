# import asyncio
# from motor.motor_asyncio import AsyncIOMotorClient
# from app.core.config import settings
# import json

# async def test_mongo():
#     print(f"Connecting to MongoDB at {settings.MONGO_URI}")
#     print(f"Database: {settings.MONGO_DB}, Collection: {settings.MONGO_COLLECTION}")
    
#     try:
#         # Create a MongoDB client
#         client = AsyncIOMotorClient(settings.MONGO_URI, serverSelectionTimeoutMS=5000)
        
#         # Access the database and collection
#         db = client[settings.MONGO_DB]
#         collection = db[settings.MONGO_COLLECTION]
        
#         # Ping the server to verify the connection
#         await client.admin.command('ping')
#         print("Successfully connected to MongoDB!")
        
#         # Fetch one document and print it
#         doc = await collection.find_one({})
#         if doc:
#             # Convert ObjectId to string for JSON serialization
#             doc['_id'] = str(doc['_id'])
#             print("\nFound 1 document:")
#             print(json.dumps(doc, indent=2))
#         else:
#             print(f"\nNo documents found in collection '{settings.MONGO_COLLECTION}'.")
            
#     except Exception as e:
#         print(f"Failed to connect to MongoDB: {e}")
#     finally:
#         client.close()

# if __name__ == "__main__":
#     asyncio.run(test_mongo())
