import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
web_page_content = response.text

soup = BeautifulSoup(web_page_content, "html.parser")
films_list = []

films_title = soup.find_all(name="h3", class_="title")
for title in films_title:
    content = title.getText()
    films_list.insert(0, content)


with open("movies.txt", "w", encoding="utf8") as file:
    for movie in films_list:
        file.write(movie+"\n")





