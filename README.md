# 🎬 Movie Roulette — 3D Vault

A cinematic 3D movie picker. Spin the vault, get a random movie recommendation based on genre and rating. Built with Three.js + FastAPI.

## Setup

### 1. Clone & install
```bash
git clone https://github.com/YOUR_USERNAME/movie-roulette
cd movie-roulette
pip install -r requirements.txt
```

### 2. Add your TMDB API key
Get a free key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

Create a `.env` file in the root:
```
TMDB_API_KEY=your_key_here
```

### 3. Run
```bash
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000)

## Stack
- **Frontend** — Three.js, vanilla JS, HTML/CSS
- **Backend** — FastAPI, httpx, python-dotenv
- **Data** — TMDB API (500k+ movies)
