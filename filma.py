import requests

api_key = "f660e8f4"  # Vendos këtu çelësin tënd OMDb

def merr_filmat():
    # Lista e filmave lokal (hardcoded)
    return [
        {"id": 1, "titulli": "Inception", "viti": 2010, "zhanri": "Sci-Fi"},
        {"id": 2, "titulli": "The Matrix", "viti": 1999, "zhanri": "Action"},
        {"id": 3, "titulli": "Interstellar", "viti": 2014, "zhanri": "Sci-Fi"},
        {"id": 4, "titulli": "The Dark Knight", "viti": 2008, "zhanri": "Action"},
        {"id": 5, "titulli": "Forrest Gump", "viti": 1994, "zhanri": "Drama"},
        {"id": 6, "titulli": "Fight Club", "viti": 1999, "zhanri": "Drama"},
        {"id": 7, "titulli": "Pulp Fiction", "viti": 1994, "zhanri": "Crime"},
        {"id": 8, "titulli": "Gladiator", "viti": 2000, "zhanri": "Action"},
        {"id": 9, "titulli": "Titanic", "viti": 1997, "zhanri": "Romance"},
        {"id": 10, "titulli": "Shutter Island", "viti": 2010, "zhanri": "Thriller"},
    ]

def merr_informacion_per_film_me_emri(emri_film):
    # Kërkon informacion në OMDb API për filmin me emrin e dhënë
    url = f"https://www.omdbapi.com/?apikey={api_key}&t={emri_film}"
    response = requests.get(url)
    return response.json()
