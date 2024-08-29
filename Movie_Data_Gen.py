import os
import json

# Define the directory path for saving HTML files
directory_path = 'cd path/to/your/directory'

def mokmobi_template(title, poster_url, rating, duration, genre, director, cast, description, imdbid):
    # Replace with your HTML Template
    html_template = f"""
<div class="rcimg-cover">
  <button id="toMiddle">
    <div class="play-video"></div>
  </button>
  <span class="bigcover"></span>
</div>
<div class="goomsite-movie">
  <div class="goomsite-left">
    <div class="rcimg">
      <div class="rec-image">
        <div class="separator" style="clear: both;">
          <div class="separator" style="clear: both;">
            <a href="{poster_url}" style="display: block; padding: 1em 0px; text-align: center;">
              <img alt="" border="0" data-original-height="660" data-original-width="440" height="320" src="{poster_url}" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="goomsite-right">
    <h1>{title}</h1>
    <fieldset class="rating">
      <input id="star5" name="rating" type="radio" value="5" />
      <label class="full"></label>
      <input checked="" id="star4" name="rating" type="radio" value="4" />
      <label class="full"></label>
      <input id="star3" name="rating" type="radio" value="3" />
      <label class="full"></label>
      <input id="star2" name="rating" type="radio" value="2" />
      <label class="full"></label>
      <input id="star1" name="rating" type="radio" value="1" />
      <label class="full"></label>
      <span class="likes">Rating {rating}</span>
      </fieldset>
    <div class="m-description">
      <span class="m-des">Type: Movie</span>
      <span class="m-des">Duration: {duration}</span>
      <span class="m-des">Genre: {genre}</span>
      <span class="m-des">Director: {director}</span>
      <span class="m-des">Lead Cast: {cast}</span>
    </div>
  </div>
</div>
<div class="postmovie">
  <h4><i class="fas fa-fire"></i> Description</h4>
  <p>{description}</p>
</div>
<div class='container-liquid pt-4 clearfix'>
  <div class='py-4 alert alert-info alert-dismissible fade show' role='alert'>
    <b>DISCLAIMER!</b> <i>This website does not host any files on its server. All content displayed on this site is provided by third-party sites and services. We do not control or endorse any content, products, or services provided by these sites. Any reliance on the content or services provided by third-party sites is done at your own risk. We recommend that you read the terms and conditions and privacy policies of any third-party site that you visit. If you have any questions or concerns about the content hosted by third-party sites, please contact the site owner or administrator directly!</i>
    <button class='close' data-dismiss='alert' type='button'>x</button>
  </div>
</div>
<div id="anc_pl">[id]
  Server1;https://vidsrc.cc/v2/embed/movie/{imdbid}|
  [/id] </div>
    """

    # Create a sanitized filename
    filename = os.path.join(directory_path, f"{title.replace(' ', '_').replace(':', '_').replace('/', '_')}.html")
    
    # Write HTML to file
    try:
        with open(filename, 'w') as file:
            file.write(html_template)
        print(f"HTML file generated: {filename}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Load movie details from JSON file
with open('movies.json', 'r') as file:
    movies = json.load(file)

# Important Keyword Arguments for your HTML Template
for movie in movies:
    mokmobi_template(
        title=movie["title"],
        poster_url=movie["poster_url"],
        rating=movie["rating"],
        duration=movie["duration"],
        genre=movie["genre"],
        director=movie["director"],
        cast=movie["cast"],
        description=movie["description"],
        imdbid=movie["imdbid"]
    )
