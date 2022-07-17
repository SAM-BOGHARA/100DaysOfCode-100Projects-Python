from bs4 import BeautifulSoup as bs
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

movies_webpage = response.text

soup = bs(movies_webpage,"html.parser")
# print(soup.prettify())


titles = soup.find_all(name = "h3",class_ ="title")
print(titles)

movie_titles = [movie.text for movie in titles]

with open("INTERMEDIATE\day45\project\movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")