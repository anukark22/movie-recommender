import requests
import os

API_KEY = os.getenv("06f1611833e407e172f50f00e90c2438")

def fetch_poster(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
        data = requests.get(url).json()

        if data["results"]:
            poster = data["results"][0].get("poster_path")
            if poster:
                return "https://image.tmdb.org/t/p/w500/" + poster
    except:
        pass

    return "https://via.placeholder.com/300x450"