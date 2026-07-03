from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE = "https://api.themoviedb.org/3"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/discover")
async def discover(
    genre: str = Query(""),
    rating: float = Query(6.0),
    page: int = Query(1),
):
    params = {
        "api_key": TMDB_API_KEY,
        "sort_by": "popularity.desc",
        "vote_count.gte": 80,
        "vote_average.gte": rating,
        "page": page,
        "language": "en-US",
    }
    if genre:
        params["with_genres"] = genre

    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            r = await client.get(f"{TMDB_BASE}/discover/movie", params=params)
            return r.json()
        except httpx.ConnectTimeout:
            return {"error": "TMDB timeout", "results": [], "total_results": 0}
        except Exception as e:
            return {"error": str(e), "results": [], "total_results": 0}

# Serve the frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")