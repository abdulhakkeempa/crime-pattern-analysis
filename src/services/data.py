from .database import get_collection
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def load_complaints():
    complaints_file = "complaints.json"
    collection = get_collection(os.getenv("DB_PATH"))

    with open(complaints_file, "r") as file:
        data = json.load(file)["complaints"]
        for complaint in data:
            complaint_text = (
                f"Category: {complaint['category']}\n"
                f"Description: {complaint['description']}\n"
                f"Victim: {complaint.get('victim', 'Unknown')}\n"
                f"Suspect: {complaint.get('suspect', 'Unknown')}"
            )
            embedding = get_embedding(complaint_text)
            collection.add(
                ids=[complaint["complaintId"]],
                embeddings=[embedding]
            )

if __name__ == "__main__":
    print(f"Creating embeddings for complaints...")
    load_complaints()
    print(f"Embeddings created successfully!")