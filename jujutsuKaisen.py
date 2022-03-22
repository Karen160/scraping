from math import inf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import requests_cache
import re

# Gère le cache
requests_cache.install_cache('demo_cache')

# On définit la page listant les informations du personnage en fonction de son nom
def get_jujutsu_page(character_name):
    page = 'https://jujutsu-kaisen.fandom.com/fr/wiki/' + character_name
    page = requests.get(page).text
    return BeautifulSoup(page, 'html.parser')


# On définit la page listant tous les personnages
def get_character_jujutsu_list_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, 'html.parser')

# On retourne toutes les informations du personnage 
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
                    information = information.get_text()
                    print(information)
                    information = information.replace("(Préquel)", "/")
                    information = re.sub("[\(\[].*?[\)\]]", "", information)
                    list_info.append(information)
    
        for i in range(0, len(list_name)):
            data[list_name[i]] = list_info[i]

    return data

# On récupère les noms des personnages en fonction de la limite renseignée
def get_character(soup, limit):
    characters = soup.find_all(class_='portal', limit= limit)
    name_list = list()
    for character in characters:
        name = character.span.get_text()
        name = name.replace(' ', '_', 1).replace('†', '')
        name_list.append(name)
    return name_list


if __name__ == "__main__":
    # On renseigne le lien contenant la liste des personnages et on récupère le nom de ceux sélectionnée
    path = r'https://jujutsu-kaisen.fandom.com/fr/wiki/Liste_des_Personnages'
    all_character = get_character(get_character_jujutsu_list_page(path), limit=20)

    # On récupère toutes les informations de nos personnages
    data_to_export = []
    for character in all_character:
        data_to_export.append(get_cara_character(character))

    # On affiche ses informations dans la console sous forme de tableau
    resultats = pd.DataFrame(data_to_export).dropna(how='all')
    resultats = resultats.fillna('X')
    print(resultats)

    # On crée un excel listant les caractéristiques des personnages affichés dans la console
    writer = pd.ExcelWriter('personnages_jujutsu_kaisen.xlsx', engine='xlsxwriter')
    resultats.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()