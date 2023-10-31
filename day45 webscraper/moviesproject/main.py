from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movie_tags = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_list = []
for tag in movie_tags:
    movie_list.append(tag.getText())
print(movie_list)
movie_list.reverse()


with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")