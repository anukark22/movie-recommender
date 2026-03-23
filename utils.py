import requests

API_KEY = "06f1611833e407e172f50f00e90c2438"

def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    data = requests.get(url).json()

    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    return "https://via.placeholder.com/300x450?text=No+Image"