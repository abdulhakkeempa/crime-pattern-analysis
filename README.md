# RAG Application

## Overview
The RAG (Retrieval-Augmented Generation) application is designed to manage and search complaints using a FastAPI backend. It utilizes OpenAI's embedding capabilities to find similar complaints based on user input and geographical location.

## Project Structure
```
rag-app
├── src
│   ├── api
│   │   └── app.py          # FastAPI application and API endpoints
│   ├── models
│   │   └── complaint.py     # Pydantic model for complaints
│   ├── services
│   │   ├── database.py      # Database initialization and interaction
│   │   ├── embeddings.py     # Function to generate text embeddings
│   │   └── filtering.py      # Function to filter complaints by location
│   └── utils
│       └── config.py        # Configuration settings and environment variable loading
├── complaints.json           # Initial complaints data in JSON format
├── .env                      # Environment variables (e.g., API keys)
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd rag-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. Run the application:
   ```
   uvicorn src.api.app:app --reload
   ```

## Usage
- The API provides an endpoint to search for similar complaints based on a description, victim, suspect, and geographical location.
- Use tools like Postman or curl to interact with the API.

## License
This project is licensed under the MIT License.