import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import json

async def fetch_data(query: dict = None, limit: int = 100):
    """
    Fetches data from MongoDB.
    
    Args:
        query: Optional MongoDB query dictionary. Defaults to {} (fetch all).
        limit: Maximum number of documents to return.
        
    Returns:
        A list of documents (dictionaries).
    """
    if query is None:
        query = {}
        
    print(f"Connecting to MongoDB at {settings.MONGO_URI}")
    print(f"Database: {settings.MONGO_DB}, Collection: {settings.MONGO_COLLECTION}")
    
    # Create a MongoDB client
    client = AsyncIOMotorClient(settings.MONGO_URI, serverSelectionTimeoutMS=5000)
    
    try:
        # Access the database and collection
        db = client[settings.MONGO_DB]
        collection = db[settings.MONGO_COLLECTION]
        
        # Ping the server to verify the connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # Fetch documents
        cursor = collection.find(query)
        documents = await cursor.to_list(length=limit)
        
        results = []
        for doc in documents:
            # Convert ObjectId to string for JSON serialization
            doc['_id'] = str(doc['_id'])
            results.append(doc)
            
        print(f"\nFound {len(results)} documents:")
        # Pretty print the results to the terminal
        if results:
            print(json.dumps(results, indent=2, default=str))
        else:
            print("No documents matched the query.")
            
        return results
            
    except Exception as e:
        print(f"Failed to connect to MongoDB or retrieve data: {e}")
        return []
    finally:
        client.close()

async def fetch_service_details(query: dict = None, limit: int = 100):
    """
    Fetches services and joins with professionals and users.
    Returns a custom mapped dictionary.
    """
    if query is None:
        query = {}
        
    client = AsyncIOMotorClient(settings.MONGO_URI, serverSelectionTimeoutMS=5000)
    
    try:
        db = client[settings.MONGO_DB]
        service_collection = db[settings.SERVICE_COLLECTION]
        
        # Aggregation pipeline
        pipeline = [
            {"$match": query},
            {
                "$lookup": {
                    "from": settings.PROFEAAIONAL_COLLECTION,
                    "localField": "professionalId",
                    "foreignField": "_id",
                    "as": "professional"
                }
            },
            {"$unwind": {"path": "$professional", "preserveNullAndEmptyArrays": True}},
            {
                "$lookup": {
                    "from": settings.USERS_COLLECTION,
                    "localField": "professional.userId",
                    "foreignField": "_id",
                    "as": "user"
                }
            },
            {"$unwind": {"path": "$user", "preserveNullAndEmptyArrays": True}},
            {"$limit": limit}
        ]
        
        cursor = service_collection.aggregate(pipeline)
        documents = await cursor.to_list(length=limit)
        
        results = []
        for doc in documents:
            prof = doc.get("professional", {})
            user_info = doc.get("user", {})
            
            # Construct the mapped object
            mapped_doc = {
                "_id": str(doc.get("_id")) if doc.get("_id") else None,
                "professionalId": str(doc.get("professionalId")) if doc.get("professionalId") else None,
                "userId": str(prof.get("userId")) if prof.get("userId") else None,
                "title": doc.get("title"),
                "description": doc.get("description"),
                "category": doc.get("category"),
                "specialization": prof.get("specialization", []),
                "workingDays": prof.get("workingDays", []),
                "bio": prof.get("bio"),
                "experience": prof.get("experience"),
                "rating": prof.get("rating"),
                "isAvailable": prof.get("isAvailable"),
                "location": user_info.get("location", {})
            }
            results.append(mapped_doc)
            
        print(f"\nFound {len(results)} service details:")
        if results:
            print(json.dumps(results, indent=2, default=str))
        else:
            print("No service details matched the query.")
            
        return results
            
    except Exception as e:
        print(f"Failed to fetch service details: {e}")
        return []
    finally:
        client.close()

if __name__ == "__main__":
    # Test the function manually
    asyncio.run(fetch_service_details({"category": "HAIRCUT"}))
