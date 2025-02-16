import chromadb

def initialize_database(db_path: str) -> chromadb.PersistentClient:
    return chromadb.PersistentClient(path=db_path)

def get_collection(db_path: str):
    client = initialize_database(db_path)
    collection = client.get_or_create_collection("complaints") 
    return collection

