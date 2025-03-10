from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from src.models.complaint import Complaint
from src.models.search import SearchRequest
from src.services.database import get_collection
from src.services.embeddings import get_embedding
from src.services.insights import analyze_case_relationships
from src.services.camera import find_cameras_in_radius
from dotenv import load_dotenv
from typing import Optional
import os
import json

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_path = os.getenv("DB_PATH")
collection = get_collection(db_path)

@app.post("/search_complaints/")
async def search_complaints(request: SearchRequest):
    description = request.description
    victim = request.victim
    suspect = request.suspect
    lat = request.lat
    lon = request.lon
    radius_km = request.radius_km or 1
    top_k = request.top_k or 3

    search_text = (
        f"Description: {description}\n"
        f"Victim: {victim or 'Unknown'}\n"
        f"Suspect: {suspect or 'Unknown'}"
    )
    search_embedding = get_embedding(search_text)
    print(collection.count())
    results = collection.query(query_embeddings=[search_embedding], n_results=top_k)
    print(results)

    if "ids" in results and results["ids"]:
        with open('complaints.json', "r") as f:
            data = json.load(f)
        matched_complaints = []
        for complaint_id in results["ids"][0]:
            found = next((c for c in data["complaints"] if c["complaintId"] == complaint_id), None)
            if found:
                matched_complaints.append(found)


        nearby_camera = find_cameras_in_radius(lat, lon, radius_km)

        return {
            "similar_complaints": matched_complaints,
            "insights": analyze_case_relationships(str(matched_complaints)),
            "nearby_cameras": nearby_camera
        }
    else:
        raise HTTPException(status_code=404, detail="No similar complaints found")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)