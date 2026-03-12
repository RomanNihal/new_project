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

if __name__ == "__main__":
    # Test the function manually
    asyncio.run(fetch_data())
