from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(url=URL)
website = response.text


soup = BeautifulSoup(website, "html.parser")

all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")
movies_titles = [movie.getText().replace("\xa0", " ") for movie in all_movies]

with open("movies.txt", "w") as file:
    for movie in movies_titles:
        file.write(movie + "\n")





