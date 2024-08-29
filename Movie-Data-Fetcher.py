import requests
import json

def fetch_genre_list(api_key):
    base_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            return {genre['id']: genre['name'] for genre in data['genres']}
        except json.JSONDecodeError:
            print("Error decoding JSON response for genres")
            return {}
    else:
        print(f"Error fetching genre list: {response.status_code}")
        return {}

def format_duration(minutes):
    if minutes == "N/A" or minutes <= 0:
        return "N/A"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}hr {mins}min" if hours > 0 else f"{mins}min"

def fetch_movie_details(api_key, movie_id):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            duration = data.get("runtime", "N/A")
            return {
                "duration": format_duration(duration),
                "description": data.get("overview", "N/A"),
                "poster_url": f"https://image.tmdb.org/t/p/original{data.get('poster_path')}"
            }
        except json.JSONDecodeError:
            print("Error decoding JSON response for movie details")
            return {}
    else:
        print(f"Error fetching movie details: {response.status_code}")
        return {}

def fetch_movie_credits(api_key, movie_id):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {
        'api_key': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            return {
                "director": next((crew['name'] for crew in data.get('crew', []) if crew['job'] == 'Director'), "N/A"),
                "cast": ", ".join(actor['name'] for actor in data.get('cast', [])[:5])  # Get top 5 actors
            }
        except json.JSONDecodeError:
            print("Error decoding JSON response for movie credits")
            return {}
    else:
        print(f"Error fetching movie credits: {response.status_code}")
        return {}

def fetch_movie_data(api_key, page, genre_map):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': api_key,
        'page': page,
        'language': 'en-US',
        'sort_by': 'popularity.desc'  # Sorting by popularity or any other criteria
    }
    response = requests.get(base_url, params=params)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        try:
            data = response.json()
            if 'results' in data:
                movies = []
                for movie in data['results']:
                    movie_id = movie.get('id')
                    details = fetch_movie_details(api_key, movie_id)
                    credits = fetch_movie_credits(api_key, movie_id)
                    genres = [genre_map.get(genre_id, 'Unknown') for genre_id in movie.get('genre_ids', [])]
                    movies.append({
                        "title": movie.get("title"),
                        "poster_url": details.get("poster_url"),
                        "rating": f"{movie.get('vote_average', 0):.1f}",  # Format rating to 1 decimal place
                        "duration": details.get("duration", "N/A"),
                        "genre": ", ".join(genres),
                        "director": credits.get("director", "N/A"),
                        "cast": credits.get("cast", "N/A"),
                        "description": details.get("description"),
                        "imdbid": movie.get("id")  # TMDb does not provide IMDb ID directly
                    })
                return movies
        except json.JSONDecodeError:
            print("Error decoding JSON response for movies")
    else:
        print(f"Error: Status code {response.status_code}")
        print(f"Response Text: {response.text}")
    return []

def save_to_json(movies, filename):
    with open(filename, 'w') as file:
        json.dump(movies, file, indent=4)

def main():
    api_key = "YOUR_API_KEY"  # Replace with your TMDb API key
    genre_map = fetch_genre_list(api_key)
    total_movies = []
    total_pages = 250  # 5000 movies / 20 movies per page
    
    for page in range(1, total_pages + 1):
        print(f"Fetching page {page}")
        movies = fetch_movie_data(api_key, page, genre_map)
        if movies:  # Check if movies is not None or empty
            total_movies.extend(movies)
    
    save_to_json(total_movies, 'movies.json')
    print(f"Saved {len(total_movies)} movies to 'movies.json'")

if __name__ == "__main__":
    main()
