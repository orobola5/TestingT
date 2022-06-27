import requests
from bs4 import BeautifulSoup

if _name_ == "_main_":

    link_of_music = []
    url = "https://soundof9ja.com/page/2/?s=hillsong"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content")
    results = results.findAll("li")

    for line in results:
        tag = line.find('a')
        music_link = tag.get('href')

        if music_link.endswith("/"):
            link_of_music.append(music_link)

    # part two
    list_of_downloadable_link = []
    for link in range(len(link_of_music)):
        url = link_of_music[link]

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('a', class_="fasc-button fasc-size-medium fasc-type-flat")

        for line in results:
            with open("music_link.txt", "a") as f:
                f.write(line.get('href') + "\n")
                list_of_downloadable_link.append(line.get('href'))
                
    for link in list_of_downloadable_link:
        print(link)