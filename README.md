# Movie Data Fetcher/HTML Generator

## Overview

***Movie Data Fetcher***:
 This script fetches movie data from The Movie Database (TMDb) API and saves the information to a JSON file. It retrieves genre lists, movie details, credits, and formats the data for easier consumption. 

***Movie HTML Generator***:
This script generates HTML files for movie details using a provided template. It reads movie information from a JSON file and creates an HTML file for each movie, saving them to a specified directory. The generated HTML files include movie details such as title, poster, rating, duration, genre, director, cast, and description.


## Features

***Movie Data Fetcher***
- **Fetch Genre List**: Retrieve a list of movie genres.
- **Fetch Movie Details**: Get details for a specific movie, including duration, description, and poster URL.
- **Fetch Movie Credits**: Retrieve the director and top cast members for a specific movie.
- **Fetch Movie Data**: Retrieve a list of movies with details and credits, sorted by popularity.
- **Save to JSON**: Save the fetched movie data to a JSON file.

***Movie HTML Generator***
- **HTML Template Customization**: Easily customize the HTML template to suit your design needs.
- **Automated HTML Generation**: Automatically generates an HTML file for each movie listed in the JSON file.
- **Error Handling**: Includes basic error handling for file writing issues.


### Requirements

>- Python 3.x
>- 'requests' library
>- JSON file containing movie details (movies.json)

You can install the required library using pip:
```
pip install requests
```


### Configuration

**API Key**: Replace the placeholder API key in the main function with your own TMDb API key.

`api_key = "YOUR_TMDB_API_KEY"`

**Directory Path**: Ensure the directory_path for saving HTML files in movie_list is correctly set and writable.

`directory_path = '/path/to/your/directory'`


### Usage

1.**Clone the Repository**:
```
git clone https://github.com/DetroiGuru/Movie-Data-Fetcher.git
```
2.**Navigate to the Project Directory**:
```
cd movie-data-fetcher
```
3.**Run the Script**:
```
python movie_data_fetcher.py
```
4.**Check the Output**:
>- The script will create a file named movies.json in the same directory.
>- HTML files for each movie will be generated in the specified directory_path.


### Setup

1.**Prepare the JSON File**:
- Ensure you have a movies.json file in the same directory as the script.
- The JSON file should contain a list of movies with the following fields:
```
[
  {
    "title": "Movie Title",
    "poster_url": "http://example.com/poster.jpg",
    "rating": "4.5",
    "duration": "120 min",
    "genre": "Action",
    "director": "Director Name",
    "cast": "Lead Actor, Lead Actress",
    "description": "Movie description here",
    "imdbid": "tt1234567"
  }
]
```
2.**Configure the Directory Path**: 
Update the directory_path variable in the script to point to the directory where you want to save the HTML files.
`directory_path = 'path/to/your/directory'`
3.**Run the Script**:
Execute the script to generate HTML files for each movie.
```
python Movie_HTML_Gen.py
```


### Script Details

***Movie Fetcher Data***
>- `fetch_genre_list(api_key)`: Retrieves a list of movie genres from TMDb.
>- `format_duration(minutes)`: Formats movie duration into hours and minutes.
>- `fetch_movie_details(api_key, movie_id)`: Retrieves detailed information about a specific movie.
>- `fetch_movie_credits(api_key, movie_id)`: Retrieves credits information, including the director and top cast members.
>- `fetch_movie_data(api_key, page, genre_map)`: Retrieves a list of movies with details and credits for a specific page.
>- `save_to_json(movies, filename)`: Saves the movie data to a JSON file.
>- `mokmobi_template(title, poster_url, rating, duration, genre, director, cast, description, imdbid)`: Generates HTML files for each movie with detailed information.
>- `main()`: The main function that orchestrates the data fetching, saving, and HTML generation process.

***Movie HTML Generator***
>- `mokmobi_template(replace w/ your html template)`: Function that generates an HTML file using the provided movie details and saves it to the specified directory.
>- `File Handling`: Writes the generated HTML to a file with a sanitized filename based on the movie title.
>- `Error Handling`: Catches and prints errors related to file permission issues or other exceptions.


### Example Usage
Assuming your movies.json contains the following data:
```
[
  {
    "title": "Inception",
    "poster_url": "http://example.com/inception.jpg",
    "rating": "8.8",
    "duration": "148 min",
    "genre": "Sci-Fi",
    "director": "Christopher Nolan",
    "cast": "Leonardo DiCaprio, Joseph Gordon-Levitt",
    "description": "A skilled thief is given a chance at redemption if he can successfully perform an inception.",
    "imdbid": "tt1375666"
  }
]
```
Running the script will generate an HTML file named Inception.html in the specified directory.


### Troubleshooting

>- Ensure your API key is valid and has not exceeded the rate limits.
>- Verify that the directory_path exists and is writable.
>- Check your network connection if you encounter errors fetching data.
>- If you encounter issues with JSON parsing or HTML file creation, ensure proper file permissions.
>- `PermissionError`: Ensure that the script has write permissions for the target directory.
>- `FileNotFoundError`: Verify that the movies.json file is located in the same directory as the script.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/DetroitGuru/Movie-Data-Fetcher/blob/v1.0.0/LICENSED.txt) file for details.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have suggestions or improvements.


## Acknowledgements
**The Movie Database** (TMDb) for providing the movie data through their API.
**Vidsrc.cc** for providing the movie streaming links.
