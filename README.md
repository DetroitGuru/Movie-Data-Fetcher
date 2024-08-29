# Movie Data Fetcher

This Python script fetches movie data from The Movie Database (TMDb) API and saves the information to a JSON file. It retrieves genre lists, movie details, credits, and formats the data for easier consumption.

## Features

- **Fetch Genre List**: Retrieve a list of movie genres.
- **Fetch Movie Details**: Get details for a specific movie, including duration, description, and poster URL.
- **Fetch Movie Credits**: Retrieve the director and top cast members for a specific movie.
- **Fetch Movie Data**: Retrieve a list of movies with details and credits, sorted by popularity.
- **Save to JSON**: Save the fetched movie data to a JSON file.

## Requirements

- Python 3.x
- `requests` library

You can install the required library using pip:

```sh
pip install requests

## Configuration


API Key: Replace the placeholder API key in the main function with your own TMDb API key.

api_key = "YOUR_TMDB_API_KEY"

Directory Path: Ensure the directory_path for saving HTML files in movie_list is correctly set and writable.

directory_path = '/path/to/your/directory'


## Usage

Clone the Repository:
git clone https://github.com/DetroiGuru/movie-data-fetcher.git

Navigate to the Project Directory:
cd movie-data-fetcher

Run the Script:
python movie_data_fetcher.py

Check the Output:
The script will create a file named movies.json in the same directory.
HTML files for each movie will be generated in the specified directory_path.

## Script Details


fetch_genre_list(api_key): Retrieves a list of movie genres from TMDb.

format_duration(minutes): Formats movie duration into hours and minutes.

fetch_movie_details(api_key, movie_id): Retrieves detailed information about a specific movie.

fetch_movie_credits(api_key, movie_id): Retrieves credits information, including the director and top cast members.

fetch_movie_data(api_key, page, genre_map): Retrieves a list of movies with details and credits for a specific page.

save_to_json(movies, filename): Saves the movie data to a JSON file.

mokmobi_template(title, poster_url, rating, duration, genre, director, cast, description, imdbid): Generates HTML files for each movie with detailed information.

main(): The main function that orchestrates the data fetching, saving, and HTML generation process.

## Troubleshooting


Ensure your API key is valid and has not exceeded the rate limits.
Verify that the directory_path exists and is writable.
Check your network connection if you encounter errors fetching data.
If you encounter issues with JSON parsing or HTML file creation, ensure proper file permissions.

## License


This project is licensed under the MIT License - see the LICENSE file for details.

## Contact


For questions or comments, please contact me t.me/detroitguru