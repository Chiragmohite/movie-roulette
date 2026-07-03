# 🎬 Movie Roulette — 3D Vault

A cinematic 3D movie discovery app. Spin the vault, watch it eliminate cards one by one, and land on your next watch — filtered by genre and rating. No more decision fatigue.

🔗 **Live Demo:** [movie-roulette-c8dx.onrender.com](https://movie-roulette-c8dx.onrender.com)

## ✨ Features

- 🌀 **3D rotating vault** of movie cards built with Three.js
- 🎰 **Spin animation** with cinematic easing — lands on a random pick
- 🎬 **Center banner popup** with poster, rating, overview and trailer link
- 🎭 **Genre filters** — Action, Comedy, Drama, Horror, Sci-Fi and more
- ⭐ **Rating filter** with auto-fallback (loosens rating if no results found)
- 🌌 **Dynamic lighting** — drifting colored lights over the 3D scene
- 🖱️ **Drag to spin** manually with momentum

## 🚀 Run Locally

```bash
git clone https://github.com/Chiragmohite/movie-roulette
cd movie-roulette
pip install -r requirements.txt
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000)

## 🔑 TMDB API Key

Get a free key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

Create a `.env` file in the root:
```
TMDB_API_KEY=your_key_here
```

## 🛠 Stack

| Layer | Tech |
|---|---|
| Frontend | Three.js, Vanilla JS, HTML/CSS |
| Backend | FastAPI, Python |
| Data | TMDB API (500k+ movies) |
| Deploy | Render |

## 📁 Structure

```
movie-roulette/
├── main.py           ← FastAPI server
├── requirements.txt
├── render.yaml       ← Render deployment config
├── .env              ← API key (not pushed)
├── .gitignore
└── static/
    └── index.html    ← 3D frontend
```