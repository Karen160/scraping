from numpy import character
import requests
from bs4 import BeautifulSoup
import pandas as pd
import itertools
# import requests_cache

# requests_cache.install_cache('demo_cache')

def get_jujutsu_page(character_name):
    page = 'https://jujutsu-kaisen.fandom.com/fr/wiki/' + character_name
    page = requests.get(page).text
    return BeautifulSoup(page, 'html.parser')


def get_character_jujutsu_list_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, 'html.parser')


def get_cara_character(character_name):
    page = get_jujutsu_page(character_name)
    data = {}

    for container in page.find_all('aside', {'class': "portable-infobox"}):
        sections = list(itertools.chain(container.find_all('section', {'class': "pi-group"}, limit=3)))
        list_name = list()
        list_info = list()
        for section in sections:
            if len(section) > 1:
                for title in section.find_all('h3'):
                    list_name.append(title.get_text())

                informations = section.find_all(class_="pi-data-value")
                for information in informations:
                    list_info.append(information.get_text().replace('[1]', ''))
    
        for i in range(0, len(list_name)):
            data[list_name[i]] = list_info[i]
    return data


def get_character(soup, limit):
    characters = soup.find_all(class_='portal', limit= limit)
    name_list = list()
    for character in characters:
        name = character.span.get_text()
        name = name.replace(' ', '_', 1).replace('†', '')
        name_list.append(name)
    return name_list


if __name__ == "__main__":
    path = r'https://jujutsu-kaisen.fandom.com/fr/wiki/Liste_des_Personnages'
    all_character = get_character(get_character_jujutsu_list_page(path), limit= 3)

    data_to_export = []

    for character in all_character:
        data_to_export.append(get_cara_character(character))

    print(pd.DataFrame(data_to_export))